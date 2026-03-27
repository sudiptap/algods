# LangGraph Interview Solutions

---

## EASY

---

### Q1: Customer Support Router — Solution

**Graph:**
```
                         ┌─→ [billing_agent] ──→ (END)
                         │
(START) → [classifier] ──┼─→ [technical_agent] → (END)
                         │
                         └─→ [general_agent] ──→ (END)
```

**State:**
```python
class State(TypedDict):
    messages: Annotated[list, add_messages]
    category: str | None  # "billing", "technical", "general"
```

**Structured Output:**
```python
class TicketClassifier(BaseModel):
    category: Literal["billing", "technical", "general"] = Field(
        ..., description="Classify the support ticket category"
    )
```

**Jinja Templates:**
```jinja
{# billing_prompt.jinja #}
You are a billing specialist for {{ company_name }}.
Help the customer with invoices, payments, refunds, and subscription changes.
Customer plan: {{ customer_plan }}
Be polite and reference their account details when possible.

{# technical_prompt.jinja #}
You are a technical support engineer for {{ product_name }}.
Help with bugs, setup issues, and troubleshooting.
Product version: {{ product_version }}
Always ask for error messages and steps to reproduce.

{# general_prompt.jinja #}
You are a friendly customer support agent for {{ company_name }}.
Handle general inquiries about the product, company, and policies.
```

**Nodes:**
```python
def classify(state: State):
    last_msg = state["messages"][-1]
    classifier = llm.with_structured_output(TicketClassifier)
    result = classifier.invoke([
        {"role": "system", "content": "Classify this support ticket."},
        {"role": "user", "content": last_msg.content}
    ])
    return {"category": result.category}

def billing_agent(state: State):
    template = jinja_env.get_template("billing_prompt.jinja")
    system_prompt = template.render(company_name="Acme", customer_plan="Pro")
    reply = llm.invoke([
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": state["messages"][-1].content}
    ])
    return {"messages": [{"role": "assistant", "content": reply.content}]}

# technical_agent and general_agent follow the same pattern
```

**Routing:**
```python
graph_builder.add_conditional_edges(
    "classifier",
    lambda state: state["category"],
    {"billing": "billing_agent", "technical": "technical_agent", "general": "general_agent"}
)
```

**Key interview points:**
- Jinja keeps prompts separate from code — easier to version, test, and update
- Structured output guarantees valid classification — no regex parsing needed
- Each agent can have different tools (billing has refund_tool, technical has log_lookup_tool)

---

### Q2: Summarize-Then-Respond Bot — Solution

**Graph:**
```
(START) → [summarizer] → [responder] → (END)
```

**State:**
```python
class State(TypedDict):
    messages: Annotated[list, add_messages]
    summary: str  # running summary of conversation
```

**Jinja Templates:**
```jinja
{# summarizer_prompt.jinja #}
Summarize this conversation into {{ max_sentences }} sentences.
Focus on: key topics discussed, decisions made, open questions.
{% if existing_summary %}
Previous summary: {{ existing_summary }}
Update it with the new messages.
{% endif %}

{# responder_prompt.jinja #}
You are a helpful assistant.
Conversation context: {{ summary }}
Respond to the user's latest message using the context above.
```

**Why this pattern?**
- Full history: 50 messages = thousands of tokens = expensive and slow
- Summary: always ~100 tokens regardless of conversation length
- Tradeoff: you lose exact details but keep the gist — good for long conversations

---

### Q3: Sentiment-Gated Escalation — Solution

**Graph:**
```
                          ┌─→ [escalation] ─┐
(START) → [classifier] ──┤                  ├─→ [send_email] → (END)
                          └─→ [thank_you] ──┘
```

**State:**
```python
class State(TypedDict):
    review_text: str
    sentiment: str | None       # "positive", "neutral", "negative"
    email_body: str | None
    customer_email: str
```

**Routing logic:**
```python
def route_by_sentiment(state: State):
    if state["sentiment"] == "negative":
        return "escalation"
    return "thank_you"

graph_builder.add_conditional_edges(
    "classifier", route_by_sentiment,
    {"escalation": "escalation", "thank_you": "thank_you"}
)
```

**Key point:** Both branches converge at `send_email` — this is a fan-in pattern. The `send_email` node doesn't care which path produced the `email_body`, it just sends it.

---

### Q4: Multi-Language Translator Pipeline — Solution

**Graph:**
```
(START) → [detect_language] → [translate] → [quality_check] → (END)
```

**State:**
```python
class State(TypedDict):
    text: str
    source_lang: str | None
    target_lang: str
    translated_text: str | None
    quality_issues: list[str]
```

**Jinja template for translation:**
```jinja
Translate the following text from {{ source_lang }} to {{ target_lang }}.
Preserve tone, idioms, and formatting.
{% if domain %}
This is a {{ domain }} document — use appropriate terminology.
{% endif %}

Text: {{ text }}
```

**Key point:** Jinja parameterization means one template handles any language pair. Without it, you'd need a separate prompt for every combination.

---

### Q5: Quiz Generator — Solution

**Graph:**
```
(START) → [generate_questions] → [review_questions] → [format_quiz] → (END)
```

**Pydantic Models:**
```python
class Option(BaseModel):
    label: str          # "A", "B", "C", "D"
    text: str
    is_correct: bool

class Question(BaseModel):
    question_text: str
    options: list[Option]
    explanation: str
    difficulty: Literal["easy", "medium", "hard"]

class Quiz(BaseModel):
    questions: list[Question]
```

**Key point:** Structured output guarantees you get valid JSON that your frontend can render directly — no parsing/regex needed.

---

## MEDIUM

---

### Q6: Research Agent with Tool Use — Solution

**Graph (has a cycle):**
```
                    ┌────────────────────────┐
                    │                        │
(START) → [agent] ──┤─→ [tools] ─── loop ───┘
                    │
                    └─→ [final_answer] → (END)

     * agent → tools → agent (repeats until done or max 5 calls)
```

**State:**
```python
class State(TypedDict):
    messages: Annotated[list, add_messages]
    tool_calls_count: int
```

**The cycle:**
```python
def should_continue(state: State):
    last_msg = state["messages"][-1]
    if state["tool_calls_count"] >= 5:
        return "final_answer"          # safety limit
    if last_msg.tool_calls:
        return "tools"                  # agent wants to use a tool
    return "final_answer"               # agent is done

graph_builder.add_conditional_edges(
    "agent", should_continue,
    {"tools": "tools", "final_answer": "final_answer"}
)
graph_builder.add_edge("tools", "agent")  # after tool runs, go back to agent
```

**How the cycle terminates:**
1. Agent decides it has enough info and responds without tool calls
2. OR the 5-call safety limit is hit

**Key interview points:**
- Always have a max iteration limit — LLMs can get stuck in loops
- The `tool_calls_count` in state tracks iterations across the cycle
- This is the most common LangGraph pattern — it's how ReAct agents work

---

### Q7: Document Review with Human-in-the-Loop — Solution

**Graph:**
```
(START) → [extract_clauses] → [flag_risks] → ⏸ HUMAN REVIEW → [generate_report] → (END)
                                                    │
                                           interrupt_before
                                      (human approves/edits/rejects)
```

**Implementation:**
```python
checkpointer = PostgresSaver(conn)

graph = graph_builder.compile(
    checkpointer=checkpointer,
    interrupt_before=["generate_report"]  # pause after human reviews flags
)
```

**Flow:**
```python
# Step 1: Run until pause
config = {"configurable": {"thread_id": "contract-123"}}
result = graph.invoke({"document": contract_text}, config)
# Graph pauses. result contains flagged clauses for human review.

# Step 2 (could be 2 days later): Human reviews and edits
graph.update_state(config, {
    "flagged_clauses": [
        {"clause": "...", "risk": "high", "human_approved": True},
        {"clause": "...", "risk": "low", "human_approved": False},  # human removed this flag
    ]
})

# Step 3: Resume
result = graph.invoke(None, config)  # generate_report runs with human-edited flags
```

**Why Postgres checkpointer?**
- Human might review 2 days later — in-memory would be lost on server restart
- Postgres survives restarts, deployments, and server crashes
- Thread ID `"contract-123"` is the lookup key

---

### Q8: Parallel Research + Synthesis — Solution

**Graph:**
```
                    ┌─→ [research_react] ──┐
                    │                      │
(START) → [fan_out] ┼─→ [research_vue] ────┼─→ [synthesize] → (END)
                    │                      │
                    └─→ [research_compare] ─┘

          * all 3 research nodes run in PARALLEL
          * synthesize waits for ALL 3 to finish
```

**State with separate keys for parallel writes:**
```python
class State(TypedDict):
    question: str
    react_findings: str | None
    vue_findings: str | None
    comparison_findings: str | None
    final_report: str | None
```

**Parallel execution in LangGraph:**
```python
# Fan-out: one node goes to multiple nodes
graph_builder.add_edge("fan_out", "research_react")
graph_builder.add_edge("fan_out", "research_vue")
graph_builder.add_edge("fan_out", "research_compare")

# Fan-in: all three must complete before synthesis
graph_builder.add_edge("research_react", "synthesize")
graph_builder.add_edge("research_vue", "synthesize")
graph_builder.add_edge("research_compare", "synthesize")
```

**Key point:** LangGraph runs nodes in parallel when they share the same source and have no dependencies. The fan-in node (`synthesize`) waits for ALL incoming edges to complete. Each parallel node writes to a DIFFERENT state key to avoid conflicts.

---

### Q9: Streaming Chat with Memory — Solution

**Graph:**
```
                          ┌─→ [therapist] ────→ (END)
(START) → [classifier] ──┤
                          └─→ [logical_agent] → (END)

Infrastructure: Postgres Checkpointer + SSE/WebSocket streaming
```

**Backend (FastAPI + SSE):**
```python
@app.get("/chat/{thread_id}")
async def chat(thread_id: str, message: str):
    config = {"configurable": {"thread_id": thread_id}}
    state = {"messages": [{"role": "user", "content": message}]}

    async def event_stream():
        async for msg, metadata in graph.astream(state, config, stream_mode="messages"):
            if msg.content:
                yield f"data: {json.dumps({'token': msg.content})}\n\n"
        yield f"data: {json.dumps({'done': True})}\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")
```

**Reconnection:** If the client disconnects, it can call `GET /state/{thread_id}` which uses `graph.get_state(config)` to fetch the last checkpointed state.

**Key points:**
- `stream_mode="messages"` for token-by-token output
- `astream` (async) for non-blocking concurrent users
- Postgres checkpointer handles persistence
- Thread ID = user's session/conversation ID

---

### Q10: Multi-Step Form with Subgraphs — Solution

**Outer Graph:**
```
(START) → [intake_subgraph] → [assess] → [process] → [notify] → (END)
```

**Inner Subgraph (intake):**
```
(START) → [ask_type] → ⏸ → [ask_date] → ⏸ → [ask_description] → ⏸ → [ask_photos] → (END)
                        │                │                        │
                  wait for user    wait for user           wait for user
```

**How subgraphs work:**
```python
# Define inner graph
intake_graph = StateGraph(IntakeState)
intake_graph.add_node("ask_type", ask_incident_type)
# ... add other nodes with interrupts
intake = intake_graph.compile(interrupt_after=["ask_type", "ask_date", "ask_description"])

# Add as node in outer graph
outer_graph.add_node("intake", intake)  # a compiled graph can be a node
```

**State flows:** The parent passes its state to the subgraph. The subgraph returns its final state back to the parent. You define input/output schemas to control what crosses the boundary.

---

### Q11: Retry and Fallback Pattern — Solution

**Graph:**
```
                          ┌──────── loop (max 3) ────────┐
                          │                              │
(START) → [book_flight] ──┤─── success ─→ [confirmation] → (END)
                          │
                          └─── retries >= 3 ─→ [fallback] → (END)
```

**State:**
```python
class State(TypedDict):
    messages: Annotated[list, add_messages]
    retry_count: int        # tracks attempts
    last_error: str | None
    booking_result: dict | None
```

**Retry logic:**
```python
def should_retry(state: State):
    if state.get("booking_result"):
        return "confirmation"
    if state["retry_count"] >= 3:
        return "fallback"
    return "book_flight"  # retry

graph_builder.add_conditional_edges(
    "book_flight", should_retry,
    {"book_flight": "book_flight", "confirmation": "confirmation", "fallback": "fallback"}
)
```

**Backoff:** Implement inside the node itself using `asyncio.sleep(2 ** retry_count)`. The graph doesn't handle timing — nodes do.

---

## HARD

---

### Q12: Multi-Agent Collaboration — Solution

**Graph:**
```
                                          ┌─── loop (max 3) ───┐
                                          │                    │
(START) → [pm_agent] → [architect] → [developer] → [reviewer] ─┤
                                                                │
                                                   approved ────→ [pm_final] → (END)
```

**Developer-Reviewer loop:**
```python
class State(TypedDict):
    feature_request: str
    tasks: list[dict]
    architecture: str
    code: dict              # task_id -> pseudocode
    review_feedback: str | None
    review_approved: bool
    review_rounds: int

def route_after_review(state: State):
    if state["review_approved"] or state["review_rounds"] >= 3:
        return "pm_final"
    return "developer"  # send back with feedback

graph_builder.add_conditional_edges(
    "reviewer", route_after_review,
    {"developer": "developer", "pm_final": "pm_final"}
)
```

**Context isolation:** Each agent gets only the state keys it needs via its Jinja template. The developer sees `tasks` + `architecture` + `review_feedback`, but not the raw `feature_request`. The reviewer sees `code` + `architecture`, but not the PM's original breakdown reasoning.

---

### Q13: RAG with Adaptive Retrieval — Solution

**Graph (two independent cycles):**
```
                                                      ┌── loop 1 (max 3) ──┐
                                                      │                    │
(START) → [generate_query] → [retrieve] → [grade_docs] ┤                    │
                                  ↑                    │                    │
                                  └── [rewrite_query] ←┘                    │
                                                                           │
                                         relevant ─→ [generate_answer] → [hallucination_check]
                                                          ↑                    │
                                                          │                    ├─ no hallucination → (END)
                                                          └── loop 2 (max 2) ──┘

     * Loop 1: rewrite query if docs are irrelevant (max 3 rewrites)
     * Loop 2: regenerate answer if hallucination detected (max 2 retries)
```

**State:**
```python
class State(TypedDict):
    question: str
    search_query: str
    documents: list[dict]
    doc_relevance: str          # "relevant" or "irrelevant"
    answer: str | None
    has_hallucination: bool
    query_rewrites: int         # max 3
    answer_regenerations: int   # max 2
```

**Two exit conditions:**
```python
def route_after_grading(state):
    if state["doc_relevance"] == "relevant":
        return "generate_answer"
    if state["query_rewrites"] >= 3:
        return "generate_answer"    # give up rewriting, use what we have
    return "rewrite_query"

def route_after_hallucination_check(state):
    if not state["has_hallucination"]:
        return "end"
    if state["answer_regenerations"] >= 2:
        return "end"                # give up, return best effort
    return "generate_answer"
```

**Key point:** Every cycle MUST have a counter + max limit. Without it, a confusing question could loop forever.

---

### Q14: Production Multi-Tenant Platform — Solution

**Architecture:**
```
┌─────────────────────────────────────────────────────────────────┐
│  Clients                                                        │
│  ┌──────────────┐  ┌──────────────────┐                         │
│  │ Browser (SSE) │  │ Mobile (WebSocket)│                        │
│  └──────┬───────┘  └────────┬─────────┘                         │
└─────────┼──────────────────┼────────────────────────────────────┘
          │                  │
          ▼                  ▼
┌─────────────────────────────────────────────────────────────────┐
│  API Layer                                                      │
│  ┌──────────────┐  ┌──────────────┐                              │
│  │  FastAPI      │→│ Rate Limiter  │                              │
│  └──────────────┘  └──────┬───────┘                              │
└───────────────────────────┼─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│  LangGraph Runtime                                              │
│  ┌──────────────┐  ┌──────────────────┐                          │
│  │ Compiled Graph│→│ Postgres          │                          │
│  │               │  │ Checkpointer     │                          │
│  └──────┬───────┘  └────────┬─────────┘                          │
└─────────┼──────────────────┼────────────────────────────────────┘
          │                  │
          ▼                  ▼
┌─────────────────────────────────────────────────────────────────┐
│  Infrastructure                                                  │
│  ┌───────────┐  ┌──────────┐  ┌───────┐  ┌──────────┐           │
│  │ PgBouncer  │→│ Postgres  │  │ Redis  │  │ LangSmith │          │
│  │ (pool)     │  │ (DB)      │  │(queue) │  │ (tracing) │          │
│  └───────────┘  └──────────┘  └───────┘  └──────────┘           │
└─────────────────────────────────────────────────────────────────┘
```

**Architecture decisions:**

**Storage:**
- Postgres with connection pooling (PgBouncer) — handles 10K threads
- Partition checkpoint table by tenant_id for query performance
- Set TTL on old checkpoints — delete conversations older than 90 days

**Thread management:**
- Thread ID format: `{tenant_id}:{conversation_id}`
- Rate limit: max 10 concurrent graphs per tenant
- Queue excess requests with a task queue (Celery/Redis)

**Observability:**
- LangSmith tracing on every graph invocation
- Custom tags: tenant_id, graph_name, node_name
- Alert on: node latency > 5s, graph step count > 20, error rate > 1%

**Streaming:**
- SSE for browser clients, WebSocket for mobile
- Redis pub/sub as middleware between graph and API layer
- On disconnect: client sends last received token index, server replays from checkpoint

**Cost control:**
- Track tokens per tenant in state
- Add a `budget_check` node early in the graph — if over budget, route to "quota exceeded" response
- Max 25 nodes per graph invocation (prevent infinite loops)

**Deployment:**
- LangGraph Cloud: faster to ship, managed infra, built-in monitoring. Use for MVP/small scale.
- Self-hosted (K8s): full control, cheaper at scale, custom checkpointer. Use for >1000 tenants or strict compliance requirements.

---

### Q15: Dynamic Graph Construction — Solution

**Graph:**
```
(START) → [planner] → [validator] ──┬─ valid ──→ [builder] → [executor] → (END)
               ↑                    │
               └──── invalid ───────┘

     builder constructs at runtime:
     ┌─────────────────────────────────┐
     │  [Node 1] → [Node 2] → [Node 3] │  (Jinja-templated nodes)
     └─────────────────────────────────┘
```

**Planner output (structured):**
```python
class NodeDef(BaseModel):
    name: str
    description: str
    prompt_template: str  # Jinja template as string

class EdgeDef(BaseModel):
    from_node: str
    to_node: str
    condition: str | None  # optional, for conditional edges

class GraphDef(BaseModel):
    nodes: list[NodeDef]
    edges: list[EdgeDef]
```

**Builder:**
```python
def build_graph(graph_def: GraphDef):
    builder = StateGraph(State)
    for node in graph_def.nodes:
        template = jinja_env.from_string(node.prompt_template)
        builder.add_node(node.name, make_node_fn(template))
    for edge in graph_def.edges:
        builder.add_edge(edge.from_node, edge.to_node)
    return builder.compile()
```

**Safety concerns:**
- Never let the LLM generate arbitrary Python — only Jinja templates
- Validate graph is a DAG (or has bounded cycles) before execution
- Sandbox execution, set max node count
- Whitelist allowed tools — don't let dynamic graphs access dangerous tools

---

### Q16: Event-Driven Agent with External Triggers — Solution

**Graph:**
```
(START) → [validate] → [process_payment] → ⏸ WAIT ──→ [reserve_inventory] → [ship] → ⏸ WAIT ──→ [confirm] → (END)
                                              ↑                                          ↑
                                       payment webhook                            shipping webhook
                                       (could take minutes)                       (could take days)
```

**Key insight:** This is NOT `interrupt_before` — that pauses for human input within the same request. This waits for **external async events** that could take hours.

**Implementation:**
- Use checkpointing to save state after `process_payment`
- Store the thread_id + expected event type in a "pending events" DB table
- Webhook endpoint receives payment confirmation, looks up thread_id, resumes graph:
  ```python
  @app.post("/webhook/payment")
  async def payment_webhook(data: PaymentResult):
      thread_id = pending_events.lookup(data.order_id)
      config = {"configurable": {"thread_id": thread_id}}
      graph.update_state(config, {"payment_status": data.status})
      await graph.ainvoke(None, config)  # resume
  ```

**Infrastructure needed:**
- Durable checkpointer (Postgres) — graph is paused for hours/days
- Event registry DB — maps external IDs to thread IDs
- Dead letter queue — handle webhooks that arrive for unknown threads
- Timeout mechanism — if no webhook after 24h, trigger cancellation flow

---

### Q17: Self-Improving Agent with Evaluation Loop — Solution

**Graph (nested loops):**
```
OUTER LOOP (max 3 — try new approaches)
│
├─→ [generate_code] → [run_tests] ──┬── pass ──→ [evaluate_quality] ──┬── score >= 7 → [return_best] → (END)
│        ↑                          │                                 │
│        │                          │                                 └── score < 7 ─→ [new_approach] ─┐
│        │          INNER LOOP      │                                                                  │
│        │        (max 5 — fix      │                                                                  │
│        │         current code)    │                                                                  │
│        │                          │                                                                  │
│        └── [read_error] ←── fail ─┘                                                                  │
│                                                                                                      │
└──────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

**State:**
```python
class State(TypedDict):
    spec: str
    current_code: str
    approach_description: str
    test_results: str
    inner_attempts: int       # resets each outer loop
    outer_attempts: int
    best_code: str            # highest scoring version so far
    best_score: int
    scores_history: list[dict]  # [{approach, code, score}]
```

**Key insight:** The inner loop state (attempt count) must reset when the outer loop starts a new approach. The `best_code` persists across both loops so you never lose a good solution.

---

### Q18: Mixture-of-Agents — Solution

**Graph:**
```
                    ┌─→ [claude_agent] ──┐
                    │                    │
(START) → [fan_out] ┼─→ [gpt_agent] ────┼─→ [judge] ──┬── confident ──→ (END)
                    │                    │              │
                    └─→ [gemini_agent] ──┘              └── not confident
                                                               │
                                              [follow_up] → [target_agent] ─── loop back to [judge]
                                                                                 (max 3 rounds)

     * All 3 agents run in PARALLEL
     * Judge picks best / synthesizes / asks follow-ups
```

**Parallel execution:**
Each agent node calls a different LLM API. LangGraph runs them in parallel. Each writes to its own state key:
```python
class State(TypedDict):
    question: str
    claude_answer: str | None
    gpt_answer: str | None
    gemini_answer: str | None
    judge_decision: dict | None  # {winner, confidence, reasoning}
    follow_up_target: str | None
    rounds: int
```

**Handling slow agents:**
- Set timeout per node (e.g., 30s)
- If one agent times out, the judge works with the answers it has
- Implement as: try/except in the node, write `"TIMEOUT"` to state if it fails

**Judge logic:**
```python
def judge(state: State):
    answers = {
        "claude": state.get("claude_answer", "TIMEOUT"),
        "gpt": state.get("gpt_answer", "TIMEOUT"),
        "gemini": state.get("gemini_answer", "TIMEOUT"),
    }
    # Remove timeouts
    valid = {k: v for k, v in answers.items() if v != "TIMEOUT"}
    # LLM evaluates and picks/synthesizes
    result = judge_llm.invoke(build_judge_prompt(state["question"], valid))
    return {"judge_decision": result}
```

**Key interview points:**
- Fan-out/fan-in is the core pattern
- Always handle the case where an agent fails/times out
- The judge itself is an LLM call — you can use structured output for its decision
- Follow-up loop adds depth but needs a max iteration limit

---

## ReAct PATTERN — Dedicated Solutions

---

### Q19: Travel Planning Agent — Solution

**Graph:**
```
              ┌─────────── ReAct loop (max 10) ──────────┐
              │                                          │
(START) → [agent] ──→ [tools] ──────────────────────────┘
              │          │
              │          ├── flight_search
              │          ├── hotel_search
              │          ├── activity_search
              │          ├── currency_converter
              │          └── weather_lookup
              │
              └──→ [format_itinerary] → (END)
```

**State:**
```python
class State(TypedDict):
    messages: Annotated[list, add_messages]
    tool_calls_count: int
    budget_remaining: float       # tracks spending across tool calls
    itinerary: dict | None        # structured final output
```

**Tool selection reasoning — what the message history looks like after 3 iterations:**
```
HumanMessage: "Plan a 5-day trip to Tokyo in March for 2, budget $3000"

AIMessage: (tool_calls: [weather_lookup("Tokyo", "March")])
    Thought: "I should check weather first to plan indoor vs outdoor activities"

ToolMessage: "Tokyo in March: 10-15°C, cherry blossom season, occasional rain"

AIMessage: (tool_calls: [activity_search("Tokyo cherry blossom spots March")])
    Thought: "Cherry blossom season! I should find outdoor activities around this"

ToolMessage: "Top spots: Ueno Park, Shinjuku Gyoen, Meguro River..."

AIMessage: (tool_calls: [hotel_search("Tokyo", "Shinjuku", "March 1-5", 2)])
    Thought: "Shinjuku is central to most spots. Let me find hotels there."

ToolMessage: "Hotel Gracery Shinjuku: $120/night, Hotel Sunroute: $95/night..."

... continues until itinerary is complete
```

**Key interview points:**
- The agent REASONS about tool ORDER — weather before activities, activities before hotels (location matters)
- `budget_remaining` in state lets the agent make cost-aware decisions
- The final `format_itinerary` node structures the raw findings into a clean day-by-day plan
- Without ReAct, a chain would rigidly go flights → hotels → activities, missing the weather → activity → hotel logic

---

### Q20: SQL Database Analyst — Solution

**Graph:**
```
              ┌─────────── ReAct loop (max 8) ───────────┐
              │                                          │
(START) → [agent] ──→ [tools] ──────────────────────────┘
              │          │
              │          ├── list_tables
              │          ├── describe_table
              │          └── run_sql_query
              │
              └──→ [format_answer] → (END)
```

**State:**
```python
class State(TypedDict):
    messages: Annotated[list, add_messages]
    tool_calls_count: int
    query_errors: list[str]       # track failed queries for learning
    tables_explored: list[str]    # avoid re-exploring same tables
```

**Typical ReAct trace for "top-selling product last quarter vs same quarter last year":**
```
Thought: First I need to understand the database schema.
Action: list_tables
Observation: ["orders", "products", "customers", "order_items"]

Thought: I need to see the orders and products schema.
Action: describe_table("orders")
Observation: columns: id, customer_id, order_date, total_amount, status

Action: describe_table("order_items")
Observation: columns: id, order_id, product_id, quantity, unit_price

Thought: Now I can query for top product last quarter.
Action: run_sql_query("SELECT p.name, SUM(oi.quantity) ... WHERE order_date BETWEEN ...")
Observation: ERROR — column "name" not found in products table

Thought: I need to check the products table schema first.
Action: describe_table("products")
Observation: columns: id, product_name, category, price

Thought: The column is product_name, not name. Let me fix the query.
Action: run_sql_query("SELECT p.product_name, SUM(oi.quantity) ... ")
Observation: "Wireless Earbuds Pro — 2,340 units"

Thought: Now same query for last year's same quarter to compare.
Action: run_sql_query("SELECT p.product_name, SUM(oi.quantity) ... WHERE order_date BETWEEN [last year] ...")
Observation: "Wireless Earbuds Pro — 1,890 units"

Thought: I have both data points. Ready to answer.
Answer: "Top seller was Wireless Earbuds Pro with 2,340 units — up 24% from 1,890 same quarter last year."
```

**Error recovery — ReAct vs Retry node (Q11):**
| ReAct error handling | Retry node (Q11) |
|---|---|
| Agent SEES the error and REASONS about the fix | Node blindly retries the same action |
| "Column not found" → agent fixes the column name | Same query runs again, fails again |
| Adaptive — learns from each failure | Mechanical — hopes transient issue resolves |
| Use for: logic errors, bad queries | Use for: network timeouts, rate limits |

**SQL injection prevention:**
```python
def run_sql_query(query: str):
    # Only allow SELECT statements
    if not query.strip().upper().startswith("SELECT"):
        return "ERROR: Only SELECT queries are allowed"
    # Run with read-only database user
    with read_only_connection() as conn:
        return conn.execute(query)
```

---

### Q21: Customer Onboarding Agent — Solution

**Graph:**
```
              ┌────────────── ReAct loop ─────────────────┐
              │                                           │
(START) → [agent] ──→ [check_tool_safety] ──→ [tools] ───┘
              │              │
              │              └─ write tool? ──→ ⏸ CONFIRM ──→ [tools]
              │
              └──→ [done] → (END)
```

**State:**
```python
class State(TypedDict):
    messages: Annotated[list, add_messages]
    tool_calls_count: int
    pending_write_action: dict | None    # tool call awaiting confirmation
    actions_completed: list[str]         # audit trail: ["account_created", "payment_charged"]
```

**Tool categorization:**
```python
READ_TOOLS = {"check_email_exists", "lookup_plan_details", "verify_promo_code"}
WRITE_TOOLS = {"create_account", "charge_payment", "send_welcome_email"}

def check_tool_safety(state: State):
    last_msg = state["messages"][-1]
    tool_call = last_msg.tool_calls[0]

    if tool_call["name"] in READ_TOOLS:
        return "tools"          # safe, execute immediately
    else:
        return "confirm"        # dangerous, ask user first
```

**Confirm-before-write flow:**
```python
# Agent wants to call create_account
# Graph pauses, shows user: "I'd like to create your account on the Pro plan at $16/mo. OK?"
# User says "yes"
# Graph resumes, executes create_account
# Agent continues ReAct loop — next might be charge_payment (another confirm)
```

**How this differs from Q7 (human-in-the-loop):**
| Q7: Human-in-the-loop | Q21: Confirm-before-write |
|---|---|
| One fixed pause point in the graph | Pause happens dynamically inside the loop |
| Human reviews accumulated output | Human approves individual actions |
| `interrupt_before` on a specific node | Conditional edge inside the ReAct cycle |
| Pause once, resume once | Could pause 3 times (one per write tool) |

**Key point:** The confirmation gate is INSIDE the ReAct loop, not around it. The agent freely reads, but pauses before every write.

---

### Q22: Competitive Intelligence Researcher — Solution

**Graph:**
```
              ┌──────────── ReAct loop (max 20) ─────────┐
              │                                          │
(START) → [agent] ──→ [tools] ──────────────────────────┘
              │          │
              │          ├── web_search
              │          ├── read_webpage
              │          ├── search_news
              │          └── search_sec_filings
              │
              └──→ [synthesize_report] → (END)
```

**State:**
```python
class State(TypedDict):
    messages: Annotated[list, add_messages]
    tool_calls_count: int
    sources: list[dict]           # [{"url": "...", "fact": "...", "retrieved_at": "..."}]
    facts_collected: dict         # {"stripe": [...], "adyen": [...]}
    contradictions: list[dict]    # [{"fact_a": ..., "fact_b": ..., "sources": [...]}]
```

**Source tracking — inside the tools node:**
```python
def tools(state: State):
    last_msg = state["messages"][-1]
    tool_call = last_msg.tool_calls[0]
    result = execute_tool(tool_call)

    # Track source
    source = {
        "url": tool_call["args"].get("url") or tool_call["args"].get("query"),
        "fact": result[:200],   # summary
        "tool": tool_call["name"],
    }
    sources = state.get("sources", []) + [source]

    return {
        "messages": [ToolMessage(result)],
        "sources": sources
    }
```

**Token management for long chains (15+ tool calls):**

This is the critical challenge. After 15 tool calls, messages could be 50K+ tokens.

```
Strategy 1: Summarize-and-trim
┌──────────────────────────────────────────────┐
│ After every 5 tool calls:                     │
│ - Summarize findings so far into a "memo"    │
│ - Remove old tool messages from history       │
│ - Keep: system prompt + memo + last 3 msgs    │
└──────────────────────────────────────────────┘

Strategy 2: Structured state, not messages
┌──────────────────────────────────────────────┐
│ Instead of relying on message history:        │
│ - Store findings in state["facts_collected"]  │
│ - Agent reads structured state, not old msgs  │
│ - Messages only carry the current step        │
└──────────────────────────────────────────────┘
```

**Preventing endless searching:**
```python
def should_continue(state: State):
    if state["tool_calls_count"] >= 20:
        return "synthesize"                      # hard limit
    if len(state["facts_collected"].get("stripe", [])) >= 5 \
       and len(state["facts_collected"].get("adyen", [])) >= 5:
        return "synthesize"                      # enough facts on both
    return "tools"
```

**Contradiction handling:**
```
Agent finds: "Stripe processes $800B annually" (source A)
Agent finds: "Stripe processes $1T annually" (source B)

→ Agent adds to contradictions list
→ Synthesis node flags it: "Sources disagree on volume ($800B vs $1T).
   Source B is more recent (2024 vs 2023). Using $1T."
```

---

### Q23: DevOps Incident Response Agent — Solution

**Graph:**
```
              ┌────── ReAct loop (max 8) ──────────────────┐
              │                                            │
(START) → [agent] ──→ [check_action_safety] ──→ [tools] ──┘
              │              │
              │              ├── safe (read) → execute immediately
              │              └── dangerous (write) → confidence check
              │                       │
              │                       ├── confidence >= 0.8 → execute + log
              │                       └── confidence < 0.8 → escalate to human
              │
              ├──→ [escalate] → (END)    (can't resolve in 5 calls)
              └──→ [resolved] → (END)
```

**State:**
```python
class State(TypedDict):
    messages: Annotated[list, add_messages]
    tool_calls_count: int
    alert: dict                       # original alert data
    investigation_log: list[str]      # human-readable audit trail
    root_cause: str | None
    confidence: float                 # 0.0 to 1.0
    actions_taken: list[dict]         # [{"action": "rollback", "deploy_id": "1234", "at": "..."}]
```

**Confidence threshold for dangerous actions:**
```python
class ActionDecision(BaseModel):
    action: str                                    # "rollback_deploy", "scale_service", etc.
    args: dict
    confidence: float = Field(..., ge=0.0, le=1.0)
    reasoning: str

def check_action_safety(state: State):
    last_msg = state["messages"][-1]
    tool_call = last_msg.tool_calls[0]

    SAFE_TOOLS = {"get_metrics", "get_logs", "get_recent_deploys"}
    DANGEROUS_TOOLS = {"rollback_deploy", "scale_service", "page_oncall"}

    if tool_call["name"] in SAFE_TOOLS:
        return "tools"

    # For dangerous tools, ask the agent for its confidence
    decision = confidence_llm.invoke(
        f"You want to {tool_call['name']}. Rate confidence 0-1 that this is correct."
    )

    if decision.confidence >= 0.8:
        return "tools"         # high confidence → auto-execute
    else:
        return "escalate"      # low confidence → page a human
```

**How this differs from Q21 (confirm-before-write):**
| Q21: Confirm before write | Q23: Confidence threshold |
|---|---|
| Always asks user | Only escalates when uncertain |
| User is always available (onboarding flow) | On-call might be asleep — minimize pages |
| Binary: confirm or deny | Gradient: 0.8+ auto, <0.8 escalate |
| No time pressure | Incident is ongoing — speed matters |

**Wrong rollback safety net:**
```python
def rollback_deploy(deploy_id: str):
    # Take a snapshot before rollback
    snapshot = capture_current_state()
    perform_rollback(deploy_id)
    # Monitor for 2 minutes — if metrics don't improve, undo
    if not metrics_improved(timeout=120):
        restore_snapshot(snapshot)
        return "Rollback didn't help. Reverted. Escalating."
    return f"Rollback of {deploy_id} successful. Latency recovering."
```

---

### Q24: Multi-Turn Negotiation Agent — Solution

**Graph:**
```
┌─────────────────── NEGOTIATION ROUND (repeats) ──────────────────────────┐
│                                                                          │
│  ┌─── ReAct research loop ───┐                                           │
│  │                           │                                           │
│  [agent] ──→ [tools] ───────┘                                            │
│     │          │                                                         │
│     │          ├── search_market_rates                                    │
│     │          ├── calculate_counter_offer                                │
│     │          ├── analyze_sentiment                                      │
│     │          └── draft_response                                        │
│     │                                                                    │
│     └──→ [present_draft] → ⏸ USER REVIEW → [send_response] ─┐           │
│                                                               │           │
│          ┌────────────────────────────────────────────────────┘           │
│          │                                                               │
│          ⏸ WAIT for other party's response                               │
│          │                                                               │
│          └──→ [receive_response] → [should_continue_negotiating?]        │
│                                          │                    │          │
│                                     yes ─┘               no ──→ (END)   │
└──────────────────────────────────────────────────────────────────────────┘
```

**State:**
```python
class State(TypedDict):
    messages: Annotated[list, add_messages]
    tool_calls_count: int

    # Negotiation-specific state
    negotiation_state: dict   # {
                              #   "our_target": 150000,
                              #   "our_walkaway": 120000,
                              #   "their_last_offer": 130000,
                              #   "our_last_offer": 145000,
                              #   "concessions_made": ["dropped signing bonus ask", ...],
                              #   "round": 3,
                              #   "max_rounds": 6,
                              # }
    sentiment_history: list[dict]   # track other party's tone over time
    market_data: dict               # cached research to avoid redundant lookups
    draft_response: str | None      # current draft for user review
```

**Interleaving ReAct with user input:**
```python
# Phase 1: ReAct loop — agent researches and drafts
#   agent → tools → agent → tools → agent (decides to draft)
#   agent calls draft_response tool → draft goes to state

# Phase 2: User review (interrupt)
graph = graph_builder.compile(
    checkpointer=checkpointer,
    interrupt_after=["present_draft"]   # pause for user to review/edit the draft
)

# Phase 3: Send and wait
#   send_response → wait for other party (another interrupt or webhook)

# Phase 4: New round
#   receive other party's reply → back to ReAct loop
```

**When to stop negotiating:**
```python
def should_continue_negotiating(state: State):
    ns = state["negotiation_state"]

    # They accepted
    if ns.get("accepted"):
        return "end"

    # We hit our walkaway
    if ns["their_last_offer"] < ns["our_walkaway"]:
        return "end"   # agent explains why we're walking away

    # Max rounds exhausted
    if ns["round"] >= ns["max_rounds"]:
        return "end"

    # Sentiment turning hostile
    recent = state["sentiment_history"][-1]
    if recent["sentiment"] == "hostile":
        return "end"

    return "research"  # another round
```

**Key interview points:**
- This is a **hybrid pattern**: ReAct (research) + human-in-the-loop (approve draft) + event-driven (wait for reply)
- The `negotiation_state` is the agent's strategic memory — persists across rounds via checkpointer
- `sentiment_history` gives the agent awareness of how the negotiation is trending
- Multiple interrupt points: once for user to review draft, once to wait for other party's response

---

## REFLEXION PATTERN — Dedicated Solutions

---

### Q25: Email Copywriter with A/B Quality — Solution

**Graph:**
```
              ┌──── Reflexion loop (max 4) ─────────────────┐
              │                                             │
(START) → [generate_email] → [evaluate_rubric] → [reflect] ┘
                                    │
                               score >= 8/10
                                    │
                              [return_best] → (END)
```

**State:**
```python
class State(TypedDict):
    product_description: str
    target_audience: str
    campaign_goal: str
    current_email: dict           # {"subject": "...", "body": "..."}
    rubric_scores: dict | None    # {"subject_urgency": 2, "body_cta": 3, ...}
    total_score: float
    reflections: list[str]        # cumulative feedback
    attempts: int
    best_email: dict
    best_score: float
```

**Rubric as structured output:**
```python
class SubjectEval(BaseModel):
    under_50_chars: int = Field(..., ge=0, le=1, description="1 if under 50 chars, 0 if not")
    creates_urgency: int = Field(..., ge=0, le=1, description="1 if creates urgency without clickbait")
    audience_match: int = Field(..., ge=0, le=1, description="1 if tone matches target audience")

class BodyEval(BaseModel):
    clear_cta: int = Field(..., ge=0, le=1, description="1 if there's a clear call to action")
    addresses_pain: int = Field(..., ge=0, le=1, description="1 if it addresses audience pain points")
    right_tone: int = Field(..., ge=0, le=1, description="1 if professional tone for audience")
    benefits_focused: int = Field(..., ge=0, le=1, description="1 if focuses on benefits not features")

class OverallEval(BaseModel):
    concise: int = Field(..., ge=0, le=1, description="1 if under 200 words")
    no_jargon: int = Field(..., ge=0, le=1, description="1 if no audience-inappropriate jargon")
    would_open: int = Field(..., ge=0, le=1, description="1 if you would open this email")

class EmailRubric(BaseModel):
    subject: SubjectEval
    body: BodyEval
    overall: OverallEval
    total: int                    # sum of all scores, out of 10
    weakest_area: str             # which section needs most work
    specific_feedback: str        # one concrete suggestion
```

**Evaluate node:**
```python
def evaluate_rubric(state: State):
    evaluator = llm.with_structured_output(EmailRubric)
    result = evaluator.invoke([
        {"role": "system", "content": "Evaluate this marketing email against the rubric. Be strict."},
        {"role": "user", "content": f"Subject: {state['current_email']['subject']}\n\n{state['current_email']['body']}"}
    ])

    best_email = state["best_email"]
    best_score = state["best_score"]
    if result.total > best_score:
        best_email = state["current_email"]
        best_score = result.total

    return {
        "rubric_scores": result.dict(),
        "total_score": result.total,
        "best_email": best_email,
        "best_score": best_score,
    }
```

**Reflect node — cumulative:**
```python
def reflect(state: State):
    scores = state["rubric_scores"]
    reflection = llm.invoke(f"""
Email scored {state['total_score']}/10.

Rubric breakdown:
{json.dumps(scores, indent=2)}

Previous reflections:
{chr(10).join(f'Attempt {i+1}: {r}' for i, r in enumerate(state['reflections']))}

What specifically needs to change? Focus on the weakest area: {scores['weakest_area']}.
Give ONE concrete rewrite suggestion, not vague advice.
""")
    return {"reflections": state["reflections"] + [reflection.content]}
```

**What stops repeated mistakes:**
- Reflections are CUMULATIVE — attempt 3 sees feedback from attempts 1 and 2
- The rubric is STRUCTURED — not "make it better" but "subject_urgency scored 0/1"
- `weakest_area` focuses each reflection on the biggest problem, not everything

**Key interview points:**
- LLM-as-judge works for subjective tasks (writing quality) when you give it a specific rubric
- Structured evaluation (Pydantic) prevents vague "7/10 good job" assessments
- Always track `best_email` — sometimes attempt 2 is better than attempt 3

---

### Q26: API Integration Builder with Test Validation — Solution

**Graph:**
```
              ┌──── Reflexion loop (max 5) ──────────────────────┐
              │                                                  │
(START) → [generate_code] → [run_tests] → [analyze_failures] ───┘
                                │
                           all tests pass
                                │
                          [return_code] → (END)
```

**State:**
```python
class State(TypedDict):
    api_spec: str
    task_description: str
    current_code: str
    test_results: list[dict]     # [{"name": "test_get_users", "passed": True, "error": None}, ...]
    tests_passed: int
    tests_total: int
    reflections: list[str]
    attempts: int
    best_code: str
    best_score: float            # tests_passed / tests_total
```

**Run tests node — OBJECTIVE evaluation:**
```python
def run_tests(state: State):
    # Execute in sandbox — real HTTP calls against mock server
    results = sandbox.execute(
        code=state["current_code"],
        test_suite="integration_tests",
        timeout=30
    )

    passed = sum(1 for r in results if r["passed"])
    total = len(results)

    best_code = state["best_code"]
    best_score = state["best_score"]
    if passed / total > best_score:
        best_code = state["current_code"]
        best_score = passed / total

    return {
        "test_results": results,
        "tests_passed": passed,
        "tests_total": total,
        "best_code": best_code,
        "best_score": best_score,
    }
```

**Analyze failures — specific reflection:**
```python
def analyze_failures(state: State):
    failed = [t for t in state["test_results"] if not t["passed"]]

    reflection = llm.invoke(f"""
Code:
{state['current_code']}

Failed tests:
{json.dumps(failed, indent=2)}

Previous reflections:
{chr(10).join(f'Attempt {i+1}: {r}' for i, r in enumerate(state['reflections']))}

For each failed test:
1. What was expected vs what happened?
2. Which line of code caused it?
3. What's the exact fix?

Do NOT repeat fixes from previous reflections that didn't work.
""")
    return {"reflections": state["reflections"] + [reflection.content]}
```

**How this differs from ReAct error handling (Q20):**
```
ReAct (Q20 - SQL agent):
┌─────────────────────────────────────────────────┐
│ Agent runs query → error → agent sees error →   │
│ agent fixes THAT error → runs again             │
│                                                  │
│ One error at a time. Stream-of-consciousness.    │
│ No big-picture analysis. No cumulative memory.   │
└─────────────────────────────────────────────────┘

Reflexion (Q26 - API builder):
┌─────────────────────────────────────────────────┐
│ Agent writes ALL code → runs ALL tests →        │
│ sees ALL failures → reflects on the PATTERN →   │
│ rewrites with full context of what went wrong    │
│                                                  │
│ Holistic. Sees all 5 test results at once.       │
│ Can spot: "3 tests fail because I forgot auth    │
│ headers" — one root cause, not 3 separate fixes. │
└─────────────────────────────────────────────────┘
```

| | ReAct error recovery | Reflexion |
|---|---|---|
| Sees errors | One at a time | All at once |
| Fixes | Incremental patches | Full rewrite with reflection |
| Memory | Recent messages only | Explicit cumulative reflections |
| Best for | Exploring unknowns | Iterating toward a known goal |

---

### Q27: Resume Tailor with Multi-Criteria Evaluation — Solution

**Graph:**
```
              ┌──── Reflexion loop (max 4) ──────────────────┐
              │                                              │
(START) → [tailor_resume] → [evaluate_5d] → [reflect] ──────┘
                                  │
                             score >= 20/25
                                  │
                            [return_best] → (END)
```

**State:**
```python
class State(TypedDict):
    master_resume: str
    job_description: str
    current_resume: str
    scores: dict | None         # {"keywords": 4, "relevance": 3, "quant": 2, "length": 5, "auth": 3}
    total_score: int
    reflections: list[str]
    attempts: int
    best_resume: str
    best_score: int
    score_history: list[dict]   # track scores per dimension per attempt
```

**Multi-dimensional evaluation:**
```python
class ResumeEval(BaseModel):
    keywords: int = Field(..., ge=1, le=5, description="Keyword match with job description")
    relevance: int = Field(..., ge=1, le=5, description="Most relevant experiences highlighted")
    quantification: int = Field(..., ge=1, le=5, description="Achievements backed by numbers")
    length: int = Field(..., ge=1, le=5, description="Appropriate length")
    authenticity: int = Field(..., ge=1, le=5, description="Sounds like a real person, not generic")
    tradeoff_warning: str | None   # "Adding more keywords might hurt authenticity"
```

**Handling trade-offs — the anti-oscillation reflection:**
```python
def reflect(state: State):
    history = state["score_history"]

    # Detect oscillation: did we improve X but regress Y?
    oscillation_warning = ""
    if len(history) >= 2:
        prev = history[-2]
        curr = history[-1]
        improved = [k for k in curr if curr[k] > prev.get(k, 0)]
        regressed = [k for k in curr if curr[k] < prev.get(k, 0)]
        if improved and regressed:
            oscillation_warning = f"""
WARNING: Oscillation detected!
Improved: {improved}
Regressed: {regressed}
You must improve {regressed} WITHOUT sacrificing {improved}.
This means finding a DIFFERENT approach, not just adding more of one thing.
"""

    reflection = llm.invoke(f"""
Resume scored {state['total_score']}/25.

Scores: {json.dumps(state['scores'])}

Score history across attempts:
{json.dumps(history, indent=2)}

{oscillation_warning}

Previous reflections:
{chr(10).join(f'Attempt {i+1}: {r}' for i, r in enumerate(state['reflections']))}

Focus on Pareto improvement — make at least one dimension better
without making any dimension worse. If two dimensions conflict,
find a creative solution that satisfies both.
""")
    return {
        "reflections": state["reflections"] + [reflection.content],
        "score_history": history + [state["scores"]],
    }
```

**What a useful reflection looks like here:**
```
BAD:  "Add more keywords and make it more authentic."
      (Contradictory. Agent will oscillate.)

GOOD: "Keywords scored 2/5 because 'distributed systems' and
       'Kubernetes' from the JD are missing. Authenticity scored
       4/5 which is good. To add keywords WITHOUT hurting
       authenticity: weave 'distributed systems' into the
       existing project description on line 3 where the user
       already describes their microservices work — this is
       authentic because they actually did this work, they
       just didn't use the exact JD terminology."
```

**Key interview points:**
- Oscillation detection is critical for multi-criteria optimization
- `score_history` lets the reflection see TRENDS, not just the current score
- Pareto improvement framing: "improve X without hurting Y"
- The `tradeoff_warning` from the evaluator gives the reflector a heads-up about conflicts

---

### Q28: Data Pipeline Generator with Execution Validation — Solution

**Graph (nested loops):**
```
OUTER LOOP (max 3 — try different transformation strategies)
│
│  ┌──── INNER Reflexion loop (max 4) ─────────────────────┐
│  │                                                       │
│  [generate_pipeline] → [stage1: runs?] → [stage2: schema?] → [stage3: data correct?]
│       ↑                     │                  │                    │
│       │                fail at any stage        │                    │
│       │                     │                  │                    │
│       │                [reflect on failure] ────┘                    │
│       │                     │                                       │
│       └─────────────────────┘                                       │
│                                                                     │
│  all 3 stages pass → [return_pipeline] → (END)                      │
│                                                                     │
│  4 inner attempts exhausted → [try_new_strategy] ─┐                 │
│                                                   │                 │
└───────────────────────────────────────────────────┘                 │
```

**State:**
```python
class State(TypedDict):
    source_schema: dict
    target_schema: dict
    sample_data: list[dict]
    current_code: str
    current_strategy: str          # "pandas", "polars", "raw python"

    # Stage results
    stage1_passed: bool            # code runs without errors
    stage1_error: str | None
    stage2_passed: bool            # output schema matches target
    stage2_diff: str | None        # what's different
    stage3_passed: bool            # output data is correct
    stage3_mismatches: list[dict]  # rows that don't match

    # Reflexion state
    reflections: list[str]
    inner_attempts: int            # resets each outer loop
    outer_attempts: int
    best_code: str
    best_stage_reached: int        # 0, 1, 2, or 3 (all pass)
```

**Three-stage evaluation:**
```python
def evaluate_stage1(state: State):
    """Does the code run without errors?"""
    try:
        result = sandbox.execute(state["current_code"], state["sample_data"])
        return {"stage1_passed": True, "stage1_error": None}
    except Exception as e:
        return {"stage1_passed": False, "stage1_error": str(e)}


def evaluate_stage2(state: State):
    """Does the output schema match?"""
    output_schema = extract_schema(sandbox.last_output)
    diff = compare_schemas(output_schema, state["target_schema"])
    if not diff:
        return {"stage2_passed": True, "stage2_diff": None}
    return {"stage2_passed": False, "stage2_diff": diff}


def evaluate_stage3(state: State):
    """Does the output data look correct?"""
    output = sandbox.last_output
    mismatches = []
    for i, (got, expected) in enumerate(zip(output, state["expected_output"])):
        if got != expected:
            mismatches.append({"row": i, "got": got, "expected": expected})
    if not mismatches:
        return {"stage3_passed": True, "stage3_mismatches": []}
    return {"stage3_passed": False, "stage3_mismatches": mismatches[:5]}
```

**Routing — which stage failed?**
```python
def route_after_eval(state: State):
    if not state["stage1_passed"]:
        return "reflect"                          # code doesn't run
    if not state["stage2_passed"]:
        return "reflect"                          # schema mismatch
    if not state["stage3_passed"]:
        return "reflect"                          # data mismatch
    return "return_pipeline"                      # all 3 pass!

def route_after_reflect(state: State):
    if state["inner_attempts"] >= 4:
        return "try_new_strategy"                 # inner loop exhausted → outer loop
    return "generate_pipeline"                    # try again
```

**How reflection differs by stage:**
```python
def reflect(state: State):
    if not state["stage1_passed"]:
        focus = f"""
Stage 1 FAILED — code doesn't run.
Error: {state['stage1_error']}
This is a syntax or runtime error. Focus on fixing the exact error.
"""
    elif not state["stage2_passed"]:
        focus = f"""
Stage 2 FAILED — code runs but output schema is wrong.
Schema diff: {state['stage2_diff']}
The code works, but produces wrong columns/types. Don't rewrite from
scratch — just fix the schema mapping.
"""
    else:
        focus = f"""
Stage 3 FAILED — code runs, schema is right, but data is wrong.
Mismatched rows: {json.dumps(state['stage3_mismatches'], indent=2)}
The structure is correct but transformation logic is wrong.
Look at the specific rows that don't match to find the pattern.
"""

    reflection = llm.invoke(f"""
{focus}

Current code:
{state['current_code']}

Strategy: {state['current_strategy']}

Previous reflections:
{chr(10).join(f'  Attempt {i+1}: {r}' for i, r in enumerate(state['reflections']))}

What specific change fixes this? Be precise — reference line numbers.
""")
    return {
        "reflections": state["reflections"] + [reflection.content],
        "inner_attempts": state["inner_attempts"] + 1,
    }
```

**Outer loop — try new strategy:**
```python
def try_new_strategy(state: State):
    strategies_tried = state.get("strategies_tried", [state["current_strategy"]])
    all_strategies = ["pandas", "polars", "raw python"]
    remaining = [s for s in all_strategies if s not in strategies_tried]

    if not remaining or state["outer_attempts"] >= 3:
        return "return_best"    # give up, return best effort

    new_strategy = remaining[0]
    return {
        "current_strategy": new_strategy,
        "strategies_tried": strategies_tried + [new_strategy],
        "reflections": [],       # reset inner reflections
        "inner_attempts": 0,     # reset inner counter
        "outer_attempts": state["outer_attempts"] + 1,
    }
```

**Inner vs outer state management:**
```
INNER state (resets each outer loop):
  - reflections: []          ← cleared so new strategy starts fresh
  - inner_attempts: 0        ← reset counter

OUTER state (persists across all loops):
  - outer_attempts: 2        ← keeps counting
  - best_code: "..."         ← never lose the best version
  - best_stage_reached: 2    ← tracks progress
  - strategies_tried: [...]  ← don't repeat strategies
```

**Key interview points:**
- Multi-stage evaluation gives granular feedback — "your code runs but the schema is wrong" is way more useful than "it failed"
- Reflection quality depends on WHICH stage failed — a runtime error needs a different analysis than a data mismatch
- Inner loop fixes the current approach; outer loop abandons it entirely
- Always reset inner state but preserve outer state (best_code, strategies_tried)

---

## MULTI-AGENT PATTERNS — Dedicated Solutions

---

### Q29: Content Production Pipeline (Supervisor) — Solution

**Graph:**
```
              ┌──────────────────────────── supervisor loop ─────────────────────────────┐
              │                                                                          │
(START) → [supervisor] ──┬─→ [researcher] ──→ [supervisor]                               │
                         ├─→ [writer] ──────→ [supervisor]                               │
                         ├─→ [editor] ──────→ [supervisor]                               │
                         └─→ finish ────────→ (END)                                      │
                                                                                         │
              * Editor can reject → supervisor sends back to writer (max 2 review rounds)│
              └──────────────────────────────────────────────────────────────────────────┘
```

**State:**
```python
class State(TypedDict):
    messages: Annotated[list, add_messages]
    content_brief: str
    research: str | None
    draft: str | None
    editor_feedback: str | None
    review_rounds: int
    final_article: str | None
```

**Supervisor as tool-caller:**
```python
# Each worker is a tool the supervisor can call
researcher_tool = Tool(
    name="researcher",
    description="Finds data, stats, and quotes. Use when you need information for the article.",
)
writer_tool = Tool(
    name="writer",
    description="Writes or rewrites the article draft. Use after research is complete.",
)
editor_tool = Tool(
    name="editor",
    description="Reviews the draft for grammar, clarity, accuracy. Use after a draft exists.",
)
finish_tool = Tool(
    name="finish",
    description="Use when the article is approved by the editor and ready to publish.",
)

def supervisor(state: State):
    response = supervisor_llm.bind_tools([
        researcher_tool, writer_tool, editor_tool, finish_tool
    ]).invoke([
        {"role": "system", "content": """You are a content production supervisor.
Workflow: research → write → edit → (revise if needed) → finish.
You have max 2 revision rounds. After 2 rounds, finish with the current draft."""},
        *state["messages"]
    ])
    return {"messages": [response]}
```

**Context isolation — each worker sees only what it needs:**
```python
def researcher(state: State):
    # Only sees the brief, NOT the draft or editor feedback
    response = researcher_llm.invoke([
        {"role": "system", "content": "You are a research assistant. Find relevant data and quotes."},
        {"role": "user", "content": f"Research this topic:\n{state['content_brief']}"}
    ])
    return {"research": response.content, "messages": [ToolMessage(response.content)]}


def writer(state: State):
    # Sees brief + research + editor feedback (if revising), NOT raw research process
    context = f"Brief: {state['content_brief']}\n\nResearch: {state['research']}"
    if state.get("editor_feedback"):
        context += f"\n\nEditor feedback (address these):\n{state['editor_feedback']}"

    response = writer_llm.invoke([
        {"role": "system", "content": "You are an article writer. Write based on the research provided."},
        {"role": "user", "content": context}
    ])
    return {"draft": response.content, "messages": [ToolMessage(response.content)]}


def editor(state: State):
    # Sees draft + brief, NOT the research or previous feedback
    response = editor_llm.invoke([
        {"role": "system", "content": """Review this draft for grammar, clarity, and accuracy.
If it's good, respond with APPROVED. If not, give specific actionable feedback."""},
        {"role": "user", "content": f"Brief: {state['content_brief']}\n\nDraft:\n{state['draft']}"}
    ])

    approved = "APPROVED" in response.content.upper()
    return {
        "editor_feedback": None if approved else response.content,
        "review_rounds": state["review_rounds"] + 1,
        "messages": [ToolMessage(response.content)],
    }
```

**Preventing supervisor bottleneck:**
- Keep the supervisor prompt SHORT — just delegation logic, not domain knowledge
- Workers do the heavy lifting (research, writing) — supervisor just routes
- Don't pass full article text through supervisor messages — store in state keys
- Supervisor reads state keys to decide, not the full message history

**Key interview points:**
- Supervisor is a tool-calling agent where workers ARE the tools
- Every worker returns to supervisor — centralized control
- Context isolation via Jinja/selective state access prevents token bloat
- Review loop: editor → supervisor → writer → editor (tracked by `review_rounds`)

---

### Q30: Customer Service Swarm — Solution

**Graph:**
```
(START) → [triage] ──→ [billing] ──→ [tools] ──→ [billing] (loop with tools)
               │            │
               │            ├──→ handoff_to_technical ──→ [technical]
               │            ├──→ handoff_to_account ────→ [account]
               │            └──→ respond (no handoff) ──→ (END)
               │
               ├──→ [technical] ──→ same pattern (tools + handoffs)
               └──→ [account] ────→ same pattern (tools + handoffs)

     * ANY agent can hand off to ANY other agent
     * 3+ handoffs → [escalate_to_human] → (END)
```

**State:**
```python
class State(TypedDict):
    messages: Annotated[list, add_messages]
    current_agent: str                 # who's currently handling
    handoff_history: list[str]         # ["triage", "billing", "technical"]
    handoff_count: int
    customer_id: str
    issue_summary: str | None          # passed between agents on handoff
```

**Handoffs as tools:**
```python
def make_handoff_tool(target_agent: str, description: str):
    def handoff():
        return f"Transferring to {target_agent}..."
    handoff.__name__ = f"handoff_to_{target_agent}"
    handoff.__doc__ = description
    return handoff

# Each agent gets handoff tools to OTHER agents (not itself)
billing_tools = [
    lookup_invoice, process_refund,                    # real tools
    make_handoff_tool("technical", "Transfer when the issue is a bug or setup problem"),
    make_handoff_tool("account", "Transfer when the customer wants to change their account"),
]

technical_tools = [
    search_docs, create_ticket,
    make_handoff_tool("billing", "Transfer when the issue is about payments or invoices"),
    make_handoff_tool("account", "Transfer when the customer wants account changes"),
]
```

**Routing with circular handoff prevention:**
```python
def route_after_agent(state: State):
    last_msg = state["messages"][-1]

    # No tool calls — agent responded directly
    if not last_msg.tool_calls:
        return "end"

    tool_name = last_msg.tool_calls[0]["name"]

    # Regular tool — execute and return to same agent
    if not tool_name.startswith("handoff_to_"):
        return "tools"

    target = tool_name.replace("handoff_to_", "")

    # Guard 1: Max total handoffs
    if state["handoff_count"] >= 3:
        return "escalate_to_human"

    # Guard 2: Ping-pong detection (A → B → A)
    if len(state["handoff_history"]) >= 2 and state["handoff_history"][-1] == target:
        return "escalate_to_human"

    # Guard 3: Already visited this agent
    if state["handoff_history"].count(target) >= 2:
        return "escalate_to_human"

    return target
```

**How a new agent picks up context:**
```python
def billing_agent(state: State):
    # Build context from handoff
    context = f"Customer ID: {state['customer_id']}"
    if state.get("issue_summary"):
        context += f"\nPrevious agent's summary: {state['issue_summary']}"

    response = billing_llm.bind_tools(billing_tools).invoke([
        {"role": "system", "content": f"""You are a billing support agent.
{context}
Review the conversation history and continue helping the customer.
If the issue isn't billing-related, hand off to the right agent."""},
        *state["messages"]
    ])

    # Update issue summary for potential future handoffs
    return {
        "messages": [response],
        "current_agent": "billing",
        "handoff_history": state["handoff_history"] + ["billing"],
        "handoff_count": state["handoff_count"] + 1,
    }
```

**Key interview points:**
- No central coordinator — agents self-organize
- Handoffs are just tools with special routing logic
- THREE guards against loops: max count, ping-pong detection, repeat visit detection
- `issue_summary` passes context between agents without sharing full internal reasoning
- Escalation is the safety net — always have a human fallback

---

### Q31: Software Development Orchestrator — Solution

**Graph:**
```
(START) → [orchestrator] → [architect] → [orchestrator] → [developer] → [orchestrator]
               ↑                                                              │
               │                                                              ▼
               │                                          [tester] → [orchestrator] → [reviewer]
               │                                                              │
               │                                              ┌───────────────┤
               │                                              │               │
               │                                         approved        rejected
               │                                              │          (max 2)
               │                                              ▼               │
               │                                           (END)    [orchestrator] → replan?
               │                                                         │          │
               │                                                    just retry   redesign needed
               │                                                         │          │
               └─────────────────────────────────────────────────────────┘          │
               └────────────────────────────────────────────────────────────────────┘
```

**State:**
```python
class State(TypedDict):
    messages: Annotated[list, add_messages]
    feature_request: str
    plan: list[dict]                  # [{"step": "design", "agent": "architect", "status": "done"}, ...]
    current_step: int
    design_doc: str | None
    code: str | None
    test_results: dict | None
    review_feedback: str | None
    review_approved: bool
    revision_count: int
    needs_replan: bool
```

**Orchestrator — plan + delegate + replan:**
```python
def orchestrator(state: State):
    # First call — make the plan
    if not state.get("plan"):
        plan = planner_llm.invoke(f"""
Create a development plan for: {state['feature_request']}
Available agents: architect, developer, tester, reviewer
Return steps in order.
""")
        return {"plan": plan.steps, "current_step": 0}

    # Returning from a worker — check results
    current_step = state["plan"][state["current_step"]]

    # Replan decision: tester found critical bug
    if current_step["agent"] == "tester" and state.get("test_results"):
        critical_bugs = [b for b in state["test_results"].get("bugs", []) if b["severity"] == "critical"]
        if critical_bugs and state["revision_count"] >= 2:
            # Patching hasn't worked twice — need to redesign
            new_plan = replanner_llm.invoke({
                "original_plan": state["plan"],
                "failure_reason": f"Critical bugs persist after {state['revision_count']} patches",
                "test_results": state["test_results"],
            })
            return {"plan": new_plan.steps, "current_step": 0, "needs_replan": False, "revision_count": 0}

    # Normal: advance to next step
    return {"current_step": state["current_step"] + 1}
```

**When to replan vs just retry:**
```
Retry (send back to developer):
  - Test finds a missing null check
  - Code review says "rename this variable"
  - Minor bugs that don't affect the design

Replan (go back to architect):
  - Test finds a fundamental design flaw (e.g., race condition)
  - Same critical bug persists after 2 patches
  - Reviewer says "this approach won't scale, need different architecture"
```

**How this differs from plain supervisor:**
```
Supervisor:                          Orchestrator:
┌─────────────────────────┐          ┌─────────────────────────────┐
│ "Who should I call next?"│          │ Has a plan:                  │
│ Decides step by step     │          │   Step 1: design (architect) │
│                          │          │   Step 2: code (developer)   │
│ No plan. Can drift.      │          │   Step 3: test (tester)      │
│ Can forget to test.      │          │   Step 4: review (reviewer)  │
│ Can call workers in      │          │                              │
│ random order.            │          │ Follows the plan.            │
│                          │          │ Can REPLAN if things change. │
└─────────────────────────┘          └─────────────────────────────┘
```

**Each worker's tool set:**
```
architect:  [search_patterns, draw_diagram, check_existing_code]
developer:  [read_file, write_file, run_code, search_code]
tester:     [run_tests, write_test, check_coverage]
reviewer:   [read_file, check_style, check_complexity]
```

---

### Q32: E-Commerce Support Hierarchy — Solution

**Graph:**
```
(START) → [CEO agent] ──┬─→ [Order Team Supervisor] ──┬─→ [order_tracker]
                        │                             ├─→ [shipping_agent]
                        │                             └─→ [returns_agent]
                        │
                        ├─→ [Payment Team Supervisor] ─┬─→ [billing_agent]
                        │                              ├─→ [fraud_agent]
                        │                              └─→ [refund_agent]
                        │
                        └─→ [Product Team Supervisor] ─┬─→ [catalog_agent]
                                                       └─→ [recommendation_agent]

     * Each team is a subgraph with its own supervisor
     * CEO routes to teams, team supervisors route to workers
     * Cross-team: CEO can call MULTIPLE teams sequentially
```

**Implementation — each team is a subgraph:**
```python
# Order team subgraph
order_team = StateGraph(TeamState)
order_team.add_node("supervisor", order_supervisor)
order_team.add_node("order_tracker", order_tracker_agent)
order_team.add_node("shipping", shipping_agent)
order_team.add_node("returns", returns_agent)
# ... edges: supervisor → workers → supervisor → finish
order_team_graph = order_team.compile()

# Same for payment and product teams
payment_team_graph = build_team_graph("payment", [billing, fraud, refund])
product_team_graph = build_team_graph("product", [catalog, recommendation])

# CEO graph — teams as nodes
ceo_graph = StateGraph(State)
ceo_graph.add_node("ceo", ceo_agent)
ceo_graph.add_node("order_team", order_team_graph)      # subgraph
ceo_graph.add_node("payment_team", payment_team_graph)   # subgraph
ceo_graph.add_node("product_team", product_team_graph)   # subgraph
```

**Cross-team issues ("charged twice + hasn't shipped"):**
```python
def ceo_agent(state: State):
    response = ceo_llm.bind_tools([
        order_team_tool,
        payment_team_tool,
        product_team_tool,
        finish_tool,
    ]).invoke([
        {"role": "system", "content": """You route customer issues to the right team.
Some issues span multiple teams — handle them SEQUENTIALLY:
1. Route to the most urgent team first
2. When that team is done, route to the next team
3. Combine results into a final response.

For "charged twice + hasn't shipped":
  → Payment team first (double charge is urgent)
  → Then Order team (check shipping status)"""},
        *state["messages"]
    ])
    return {"messages": [response]}
```

**How deep can nesting go?**
```
2 levels (CEO → team supervisor → worker): GOOD
  - 3 LLM calls per routing decision
  - Clear hierarchy, debuggable

3 levels (CEO → dept → team → worker): RISKY
  - 4+ LLM calls just to route
  - Each level adds latency
  - Diminishing returns on specialization

Rule of thumb: max 2 levels of supervisor nesting.
Beyond that, flatten by giving team supervisors more workers
instead of adding more levels.
```

**When team supervisor escalates to CEO vs handles locally:**
```python
def order_supervisor(state: TeamState):
    # Handle locally: issues within the team's domain
    # Escalate: cross-team issues, unknown issues, policy exceptions

    if issue_needs_other_team(state):
        return {"escalate_to_ceo": True, "reason": "Customer also has a payment issue"}

    if issue_is_policy_exception(state):
        return {"escalate_to_ceo": True, "reason": "Customer requesting exception to return policy"}

    # Otherwise, handle locally
    return delegate_to_worker(state)
```

**Key interview points:**
- Each team is a compiled subgraph — self-contained, independently testable
- CEO handles cross-team coordination by calling teams sequentially
- 2 levels max — beyond that, flatten the hierarchy
- Escalation from team → CEO for cross-team issues and policy exceptions

---

### Q33: Research Debate System — Solution

**Graph:**
```
(START) → [advocate] → [critic] → [advocate] → [critic] → [advocate] → [critic] → [judge] → (END)
               │            │          │            │          │            │
               └─ round 1 ──┘          └─ round 2 ──┘          └─ round 3 ──┘

     * 3 rounds of back-and-forth
     * Each agent sees the OTHER's previous arguments
     * Judge reads the full debate transcript
```

**State:**
```python
class State(TypedDict):
    question: str
    debate_history: list[dict]    # [{"agent": "advocate", "round": 1, "argument": "..."}, ...]
    current_round: int
    max_rounds: int               # 3
    judge_verdict: dict | None    # {"recommendation": "...", "reasoning": "...", "confidence": 0.8}
```

**Advocate and Critic — see each other's arguments:**
```python
def advocate(state: State):
    opponent_args = [d["argument"] for d in state["debate_history"] if d["agent"] == "critic"]

    prompt = f"""You are arguing FOR the proposition: {state['question']}

Round {state['current_round']} of {state['max_rounds']}.

{"The critic's arguments so far:" if opponent_args else "You go first."}
{chr(10).join(f'Round {i+1}: {a}' for i, a in enumerate(opponent_args))}

Make your strongest argument. If the critic raised valid points, acknowledge them
but explain why the benefits still outweigh the costs. Bring NEW evidence each round,
don't just repeat yourself."""

    response = llm.invoke(prompt)
    entry = {"agent": "advocate", "round": state["current_round"], "argument": response.content}
    return {"debate_history": state["debate_history"] + [entry]}


def critic(state: State):
    advocate_args = [d["argument"] for d in state["debate_history"] if d["agent"] == "advocate"]

    prompt = f"""You are arguing AGAINST the proposition: {state['question']}

Round {state['current_round']} of {state['max_rounds']}.

The advocate's arguments so far:
{chr(10).join(f'Round {i+1}: {a}' for i, a in enumerate(advocate_args))}

Counter each point with evidence. Raise risks, costs, and alternatives
the advocate hasn't considered. Be specific, not just contrarian."""

    response = llm.invoke(prompt)
    entry = {"agent": "critic", "round": state["current_round"], "argument": response.content}
    return {
        "debate_history": state["debate_history"] + [entry],
        "current_round": state["current_round"] + 1,
    }
```

**Judge — reads full debate, produces balanced verdict:**
```python
def judge(state: State):
    transcript = ""
    for entry in state["debate_history"]:
        transcript += f"\n[{entry['agent'].upper()} — Round {entry['round']}]\n{entry['argument']}\n"

    response = judge_llm.with_structured_output(Verdict).invoke(f"""
You are an impartial judge. Read this debate and produce a balanced recommendation.

Question: {state['question']}

Full debate transcript:
{transcript}

Your job:
1. Identify the strongest arguments from each side
2. Identify weak arguments or logical fallacies
3. Weigh the evidence
4. Produce a nuanced recommendation (not just "yes" or "no")
""")
    return {"judge_verdict": response.dict()}
```

**Preventing the debate from going in circles:**
```python
def advocate(state: State):
    # Track arguments made to prevent repetition
    my_previous_args = [d["argument"] for d in state["debate_history"] if d["agent"] == "advocate"]

    prompt = f"""...
YOUR previous arguments (DO NOT repeat these — make NEW points):
{chr(10).join(f'Round {i+1}: {a[:100]}...' for i, a in enumerate(my_previous_args))}

If you have no new points to make, concede the debate.
"""
```

**When adversarial multi-agent is better than a single agent:**
```
Single agent asked "Should we migrate to microservices?":
  → Tends to pick one side and argue for it
  → Confirmation bias — once it starts saying "yes", it keeps saying "yes"
  → Misses counterarguments

Debate between advocate + critic:
  → FORCED to consider both sides
  → Critic catches weaknesses the advocate would ignore
  → Judge synthesizes — no single-agent bias
  → Better for: controversial decisions, risk assessment, strategy questions

NOT worth it for:
  → Factual questions ("what's the capital of France?")
  → Simple tasks where there's one right answer
  → Cost-sensitive: 7+ LLM calls (3 rounds × 2 agents + judge)
```

---

### Q34: Autonomous Data Analytics Team — Solution

**Graph (mixed patterns):**
```
                              ORCHESTRATOR (PM plans + assigns)
                                    │
              ┌─────────────────────┼─────────────────────┐
              │                     │                     │
         [SQL Agent]          [Viz Agent]          [Insight Agent]
         (ReAct loop)         (ReAct loop)              │
              │                     │                    │
         ┌────┤                     │                    ▼
         │    │          peer-to-peer request       [Reviewer]
         │    ▼               for data                  │
    [SQL Agent 2] ←───────────────┘                     │
    (different DB)                                  approved?
     swarm handoff                                  │      │
                                                   yes     no
                                                    │      │
                                                  (END)  (back to PM)


     * PM orchestrates the overall flow
     * Agents can talk peer-to-peer for small requests
     * SQL Agent can hand off to SQL Agent 2 (swarm pattern)
```

**State:**
```python
class State(TypedDict):
    messages: Annotated[list, add_messages]
    business_question: str
    plan: list[dict]
    current_step: int

    # Shared knowledge base — all agents can read/write
    knowledge_base: dict          # {"tables_explored": [...], "query_results": [...],
                                  #  "charts_created": [...], "insights": [...]}

    # Agent-specific state
    sql_agent_state: dict
    viz_agent_state: dict

    # Coordination
    peer_requests: list[dict]     # [{"from": "viz", "to": "sql", "request": "get monthly revenue data"}]
    handoff_target: str | None
```

**Where to draw the line — PM vs peer-to-peer:**
```python
GOES_THROUGH_PM = [
    "Starting a new analysis phase",
    "Major direction change",
    "Assigning work to an agent for the first time",
    "Deciding the analysis is complete",
    "Resolving conflicts between agent findings",
]

PEER_TO_PEER_OK = [
    "Viz agent needs specific data from SQL agent",
    "Insight agent needs a chart redone with different axes",
    "SQL agent needs to hand off to SQL Agent 2 for a different database",
]
```

**Peer-to-peer request mechanism:**
```python
def viz_agent(state: State):
    # Viz agent is building a chart but needs more data
    response = viz_llm.bind_tools([
        create_chart,
        format_chart,
        # Peer request tool — doesn't go through PM
        request_data_from_sql,
    ]).invoke(state["messages"])

    if has_tool_call(response, "request_data_from_sql"):
        # Route directly to SQL agent, skip PM
        peer_request = {
            "from": "viz",
            "to": "sql",
            "request": response.tool_calls[0]["args"]["query_description"],
        }
        return {"peer_requests": state["peer_requests"] + [peer_request]}

    return {"messages": [response]}


def route_after_viz(state: State):
    if state.get("peer_requests") and state["peer_requests"][-1]["to"] == "sql":
        return "sql_agent"       # direct to SQL, bypass PM
    return "pm_agent"            # normal: back to PM
```

**SQL Agent swarm handoff (to different DB):**
```python
def sql_agent(state: State):
    response = sql_llm.bind_tools([
        list_tables, describe_table, run_sql_query,
        # Swarm handoff — data is in a different database
        handoff_to_sql_agent_2,
    ]).invoke(state["messages"])

    if has_tool_call(response, "handoff_to_sql_agent_2"):
        return {
            "handoff_target": "sql_agent_2",
            "messages": [response],
        }
    return {"messages": [response]}
```

**Shared knowledge base — how agents coordinate:**
```python
def sql_agent(state: State):
    # Read from knowledge base
    already_queried = state["knowledge_base"].get("query_results", [])

    response = sql_llm.invoke(f"""
Previously queried data (don't re-query):
{json.dumps(already_queried, indent=2)}

New task: {state['plan'][state['current_step']]['task']}
""")

    # Write results back to knowledge base
    kb = state["knowledge_base"]
    kb["query_results"] = kb.get("query_results", []) + [{"query": "...", "result": response.content}]
    return {"knowledge_base": kb, "messages": [response]}
```

**Key interview points:**
- This is a REALISTIC system — not every interaction needs the PM
- PM handles strategy (what to analyze), agents handle tactics (how to query/chart)
- Peer-to-peer for small data requests prevents PM bottleneck
- Swarm handoff for the SQL agents mirrors real-world "this data is in a different system"
- Shared knowledge base prevents redundant work (SQL agent doesn't re-query what's already known)
- The line between "go through PM" and "talk directly" is: does this change the plan? If yes → PM. If no → peer-to-peer.
