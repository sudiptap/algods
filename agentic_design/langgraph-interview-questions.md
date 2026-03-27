# LangGraph System Design Interview Questions

---

## EASY — Must Know (Fundamentals)

### Q1: Customer Support Router
**Topics:** Nodes, edges, conditional routing, state, Jinja prompts

Design a customer support bot that:
- Takes a user message
- Classifies it into: billing, technical, or general
- Routes to the appropriate specialist agent
- Each agent has a different Jinja system prompt template
- Returns the response

Draw the graph. Define the state. Write the node functions and Jinja templates.

---

### Q2: Summarize-Then-Respond Bot
**Topics:** Sequential nodes, state accumulation, Jinja templates

Design a bot where:
- Node 1: Summarizes the conversation so far into a short context string
- Node 2: Uses that summary + the latest user message to generate a response
- The summary is stored in state and updated each turn

Why is this useful vs. just sending the full message history every time?

---

### Q3: Sentiment-Gated Escalation
**Topics:** Conditional edges, structured output, simple branching

Design a system where:
- A user writes a product review
- Node 1 classifies sentiment: positive, neutral, negative
- If negative: route to an "escalation" node that drafts an apology + discount offer
- If positive/neutral: route to a "thank you" node
- Both end at a "send_email" node

Define the state, graph, and Jinja templates for each agent persona.

---

### Q4: Multi-Language Translator Pipeline
**Topics:** Linear graph, state design, parameterized Jinja templates

Design a pipeline that:
- Takes text + target language as input
- Node 1: Detects the source language
- Node 2: Translates the text
- Node 3: Quality-checks the translation and flags issues

The Jinja prompt for Node 2 should be parameterized: `Translate from {{ source_lang }} to {{ target_lang }}`.

---

### Q5: Quiz Generator
**Topics:** State schema, sequential nodes, structured output

Design a system that:
- Takes a topic as input (e.g., "photosynthesis")
- Node 1: Generates 5 multiple-choice questions (structured output)
- Node 2: Reviews questions for accuracy and difficulty balance
- Node 3: Formats them into a final quiz

Define the Pydantic models for structured output and the state schema.

---

## MEDIUM — Intermediate (Production Patterns)

### Q6: Research Agent with Tool Use
**Topics:** Tool calling, cycles/loops, conditional exit, state

Design a research agent that:
- Takes a user question
- Has access to tools: `web_search`, `wikipedia_lookup`, `calculator`
- The agent can call tools in a loop until it has enough info
- A "should_continue" check decides: call another tool or generate final answer
- Max 5 tool calls to prevent infinite loops

Draw the graph (it has a cycle). How does the cycle terminate?

---

### Q7: Document Review Pipeline with Human-in-the-Loop
**Topics:** interrupt_before, state editing, resume, checkpointing

Design a legal document review system:
- Node 1: AI extracts key clauses from a contract
- Node 2: AI flags risky clauses
- **PAUSE** — human lawyer reviews flagged clauses
- Human can approve, edit, or add more flags
- Node 3: AI generates a summary report of approved flags

How do you implement the pause? What happens if the human edits the state? What if they walk away for 2 days — how is the state preserved?

---

### Q8: Parallel Research + Synthesis
**Topics:** Parallel node execution, fan-out/fan-in, state merging

Design a system that:
- Takes a complex question (e.g., "Compare React vs Vue for enterprise apps")
- Fans out to 3 parallel research nodes: `research_react`, `research_vue`, `research_comparison`
- Each returns findings into state
- A synthesis node combines all 3 into a final report

How do you handle parallel execution in LangGraph? How does state merging work when multiple nodes write to the same state?

---

### Q9: Streaming Chat with Memory
**Topics:** Streaming, checkpointing, thread IDs, token-by-token output

Design a chatbot for a SaaS product where:
- Multiple users chat simultaneously (thread IDs)
- Responses stream token-by-token to the frontend via SSE
- Conversation history persists across sessions (Postgres checkpointer)
- If the server restarts mid-response, the user can re-fetch the last state

Sketch the architecture. What stream_mode do you use? How does the frontend consume it?

---

### Q10: Multi-Step Form Assistant
**Topics:** Subgraphs, state handoff, interrupt patterns

Design an insurance claim assistant:
- Main graph: `intake -> assess -> process -> notify`
- The `intake` node is itself a **subgraph** that collects info step-by-step:
  - Ask for incident type -> Ask for date -> Ask for description -> Ask for photos
  - Each step interrupts and waits for user input
- Once intake is complete, the outer graph continues

How do subgraphs work? How does state flow between parent and child graph?

---

### Q11: Retry and Fallback Pattern
**Topics:** Error handling, conditional routing, retry logic

Design a system where:
- Node 1 calls an external API (e.g., flight booking)
- If it fails: retry up to 3 times with exponential backoff
- If still failing: route to a "fallback" node that apologizes and creates a support ticket
- If success: route to "confirmation" node

How do you track retry count in state? How do you implement backoff without blocking the graph?

---

## HARD — Expert (Architecture & Scale)

### Q12: Multi-Agent Collaboration System
**Topics:** Agent-as-node, delegation, shared state, dynamic routing

Design a software development team simulation:
- **PM Agent**: Takes a feature request, breaks it into tasks
- **Architect Agent**: Reviews tasks, suggests technical approach
- **Developer Agent**: Writes pseudocode for each task
- **Reviewer Agent**: Reviews the pseudocode, can send it BACK to Developer with feedback
- **PM Agent** does a final check

The Developer <-> Reviewer loop can repeat up to 3 times. Draw the graph. How do you handle the review loop? How does each agent access only the context it needs?

---

### Q13: RAG Pipeline with Adaptive Retrieval
**Topics:** Cycles, tool use, self-reflection, grading, dynamic decisions

Design a RAG system that:
- Node 1: Generates a search query from the user question
- Node 2: Retrieves documents
- Node 3: Grades relevance of retrieved docs (structured output)
- If docs are irrelevant: **rewrite the query** and loop back to Node 2 (max 3 attempts)
- If docs are relevant: Node 4 generates answer
- Node 5: Hallucination check — does the answer match the docs?
- If hallucination detected: regenerate (loop back to Node 4, max 2 attempts)
- Final node: Return answer with citations

Draw the full graph with all cycles and exit conditions. How do you prevent infinite loops?

---

### Q14: Production Deployment — Multi-Tenant Agent Platform
**Topics:** Checkpointing at scale, thread management, observability, deployment

You're building a platform where 10,000 users each have their own persistent agent. Design:
- State storage: Postgres checkpointer with connection pooling
- Thread management: How do you handle 10K concurrent threads?
- Observability: How do you trace which node is slow? (LangSmith integration)
- Streaming: SSE to frontend, handling disconnects and reconnects
- Cost control: Token budgets per user, max graph steps
- Deployment: LangGraph Cloud vs self-hosted, when to use which

This is an architecture discussion — no code needed, but justify every decision.

---

### Q15: Dynamic Graph Construction
**Topics:** Runtime graph building, meta-agents, tool generation

Design a system where:
- The user describes a workflow in natural language: "First research the topic, then write a blog post, then translate it to Spanish and French"
- A **planner agent** parses this into a graph definition (nodes + edges)
- The graph is **constructed dynamically** at runtime
- Each node is an LLM call with a Jinja template generated from the plan

How do you go from natural language -> graph? How do you generate Jinja templates dynamically? What are the safety concerns?

---

### Q16: Event-Driven Agent with External Triggers
**Topics:** Async execution, external events, long-running workflows, persistence

Design an order fulfillment system:
- Graph starts when an order is placed
- Node 1: Validate order -> Node 2: Process payment
- **WAIT** for payment webhook (could take minutes)
- Node 3: Reserve inventory -> Node 4: Ship
- **WAIT** for shipping carrier callback
- Node 5: Send confirmation to customer

The graph can be paused for hours/days waiting for external events. How do you model this? How is this different from `interrupt_before`? What infrastructure do you need?

---

### Q17: Self-Improving Agent with Evaluation Loop
**Topics:** Outer evaluation loop, state persistence across runs, feedback incorporation

Design a code generation agent that:
- Generates code based on a spec
- Runs the code in a sandbox
- If tests fail: reads the error, modifies the code, retries (inner loop, max 5 attempts)
- After each successful run: an evaluator scores the code quality (1-10)
- If score < 7: the agent gets the feedback and tries a new approach (outer loop, max 3 attempts)
- The best-scoring version is returned

Draw the nested loop structure. How do you manage state for inner vs outer loops?

---

### Q18: Mixture-of-Agents Architecture
**Topics:** Parallel agents, aggregation, voting/consensus, quality control

Design a system where:
- A user asks a complex question
- 3 different LLMs (Claude, GPT, Gemini) each generate an answer **in parallel**
- A **judge agent** evaluates all 3 answers
- The judge either picks the best one, or synthesizes a combined answer
- If the judge is not confident: it sends targeted follow-up questions to specific agents and re-evaluates

How do you fan-out to parallel agents? How does the judge decide? How do you handle one agent being much slower than the others?

---

## ReAct PATTERN — Dedicated Questions

These questions specifically test your understanding of the **Reasoning + Acting loop** —
the most common agentic pattern. Each one layers on additional complexity.

---

### Q19: Travel Planning Agent
**Topics:** ReAct loop, multiple tools, tool selection reasoning, state

Design a travel planning agent that:
- Takes a user request like "Plan a 5-day trip to Tokyo in March for 2 people, budget $3000"
- Has access to tools: `flight_search`, `hotel_search`, `activity_search`, `currency_converter`, `weather_lookup`
- The agent must reason about WHICH tool to call and in WHAT ORDER (e.g., check weather first to decide activities, then book hotels near those activities)
- Loop until a complete itinerary is built
- Max 10 tool calls

Draw the ReAct graph. How does the agent decide which tool to call next? What does the message history look like after 3 iterations? How do you structure the final output?

---

### Q20: SQL Database Analyst
**Topics:** ReAct loop, tool output as context, error recovery within the loop

Design an agent that answers business questions by querying a SQL database:
- Tools: `list_tables`, `describe_table`, `run_sql_query`
- The agent must: explore the schema first, write a query, run it, and interpret the results
- If the SQL query fails (syntax error, timeout): the agent sees the error and tries a corrected query
- If the results don't fully answer the question: the agent writes a follow-up query

Example: "What was our top-selling product last quarter, and how does it compare to the same quarter last year?"

How does the ReAct loop handle SQL errors gracefully? What's the difference between the agent retrying vs. a retry node (like Q11)? How do you prevent SQL injection?

---

### Q21: Customer Onboarding Agent
**Topics:** ReAct loop with side effects, confirmation before acting, tool categories (read vs write)

Design an agent that onboards new customers:
- **Read tools** (safe): `check_email_exists`, `lookup_plan_details`, `verify_promo_code`
- **Write tools** (side effects): `create_account`, `charge_payment`, `send_welcome_email`
- The agent should freely use read tools, but MUST get confirmation before calling any write tool

Example flow: User says "Sign me up for the Pro plan with code SAVE20"
- Agent checks if email exists (read) → verifies promo code (read) → looks up plan price (read)
- Agent says "I'll create your account and charge $16/mo. Confirm?"
- User confirms → agent calls create_account (write) → charge_payment (write) → send_welcome_email (write)

How do you implement "confirm before write" inside a ReAct loop? Is this human-in-the-loop or something different? How do you categorize tools as safe vs unsafe?

---

### Q22: Competitive Intelligence Researcher
**Topics:** ReAct with long chains, source tracking, multi-step reasoning, token management

Design a research agent that:
- Takes a query like "Compare Stripe vs Adyen for a European marketplace startup"
- Tools: `web_search`, `read_webpage`, `search_news`, `search_sec_filings`
- The agent must gather info from multiple sources, cross-reference facts, and build a structured report
- Each piece of information must be tagged with its source URL
- The agent can take 15+ tool calls for a thorough report

Challenges to address:
- How do you manage token usage when the message history grows large after 15+ tool calls?
- How do you ensure the agent doesn't keep searching forever and actually synthesizes?
- How do you track which facts came from which source?
- What if two sources contradict each other?

---

### Q23: DevOps Incident Response Agent
**Topics:** ReAct with real-time data, time-sensitive decisions, escalation logic

Design an agent that responds to production incidents:
- Tools: `get_metrics(service, timerange)`, `get_logs(service, timerange)`, `get_recent_deploys`, `rollback_deploy(deploy_id)`, `scale_service(service, replicas)`, `page_oncall(team)`
- The agent investigates the incident using the ReAct loop: check metrics → check logs → identify root cause
- Some tools are **dangerous** (`rollback_deploy`, `scale_service`) — require confidence threshold
- If the agent can't identify the root cause in 5 tool calls, it must escalate to on-call

Example: Alert fires "API latency > 2s for 5 minutes"
```
Thought: Check API metrics to see the latency pattern
Action: get_metrics("api-gateway", "last_30m")
Observation: Latency spiked at 14:32, correlates with...

Thought: Check if there was a recent deploy
Action: get_recent_deploys
Observation: Deploy #1234 went out at 14:30...

Thought: High confidence this deploy caused it. Rolling back.
Action: rollback_deploy("1234")
```

How do you implement a confidence threshold for dangerous actions? How is this different from Q21's confirmation pattern? What if the agent is wrong and rolls back a good deploy?

---

### Q24: Multi-Turn Negotiation Agent
**Topics:** ReAct loop interleaved with user interaction, strategy state, dynamic tool behavior

Design an agent that negotiates on behalf of a user (e.g., salary negotiation, vendor pricing):
- Tools: `search_market_rates`, `calculate_counter_offer`, `analyze_sentiment(message)`, `draft_response`
- The agent alternates between:
  - **Research phase** (ReAct loop): gather market data, analyze the other party's last message
  - **Response phase**: draft a response, get user approval, send it
- The agent maintains a `negotiation_state` tracking: current offer, target, walkaway price, concessions made
- Multiple rounds: other party responds → agent researches → drafts counter → user approves → repeat

How do you model the interleaving of ReAct loops with user input? How does state persist across negotiation rounds? How does the agent know when to stop negotiating?

---

## REFLEXION PATTERN — Dedicated Questions

These questions test your understanding of **self-evaluation feedback loops** —
where the agent evaluates its own output, reflects on what went wrong, and iterates.

---

### Q25: Email Copywriter with A/B Quality
**Topics:** Reflexion loop, LLM-as-judge evaluation, rubric-based scoring, cumulative reflection

Design an email marketing agent that:
- Takes a product description + target audience + campaign goal (e.g., "Drive sign-ups for our AI coding tool, targeting senior engineers")
- Generates a marketing email (subject line + body)
- Evaluates the email against a rubric:
  - Subject line: under 50 chars, creates urgency, not clickbaity (0-3)
  - Body: clear CTA, addresses pain points, matches audience tone (0-4)
  - Overall: concise (under 200 words), no jargon mismatch (0-3)
- If score < 8/10: reflects on what's weak and rewrites
- Max 4 attempts, return the highest-scoring version

How do you design the rubric as structured output? How do reflections accumulate across attempts? What stops the agent from making the same mistake twice?

---

### Q26: API Integration Builder with Test Validation
**Topics:** Reflexion with objective evaluation (real tests), code generation, error analysis

Design an agent that generates API integration code:
- Input: an API spec (OpenAPI/Swagger) + a description of what the integration should do
- The agent writes Python code that calls the API
- Evaluation: run the code in a sandbox against a mock server
  - Does it make the right HTTP calls? (check method, path, headers)
  - Does it handle the response correctly? (parse JSON, extract fields)
  - Does it handle errors? (timeout, 4xx, 5xx)
- 5 test cases run automatically. Score = tests passed / total
- If score < 1.0: reflect on which tests failed and why, then regenerate
- Max 5 attempts

How is this different from ReAct error handling? The evaluation is OBJECTIVE (real tests), not the LLM guessing. How do you structure the reflection to be specific enough that the next attempt actually fixes the issue?

---

### Q27: Resume Tailor with Multi-Criteria Evaluation
**Topics:** Reflexion with multi-dimensional scoring, weighted criteria, Pareto improvement

Design an agent that tailors a resume for a specific job posting:
- Input: user's master resume + job description
- Agent rewrites the resume to emphasize relevant experience
- Evaluation on 5 dimensions (each 1-5):
  - **Keyword match**: does it include key terms from the job description?
  - **Relevance**: are the most relevant experiences highlighted?
  - **Quantification**: are achievements backed by numbers?
  - **Length**: appropriate length (not too long, not too short)?
  - **Authenticity**: does it still sound like the person, not generic?
- Total score out of 25. Threshold: 20
- The challenge: improving one dimension often HURTS another (adding keywords reduces authenticity, adding numbers increases length)

How does the agent handle trade-offs between competing criteria? How do you prevent oscillation (improve keywords → hurts authenticity → improve authenticity → hurts keywords → ...)? What does a useful reflection look like here?

---

### Q28: Data Pipeline Generator with Execution Validation
**Topics:** Reflexion + Plan-and-Execute hybrid, multi-stage evaluation, nested loops

Design an agent that builds data transformation pipelines:
- Input: source schema (CSV columns) + desired output schema + sample data
- The agent writes a pandas transformation pipeline
- **Stage 1 evaluation**: Does the code run without errors?
- **Stage 2 evaluation**: Does the output schema match the desired schema?
- **Stage 3 evaluation**: Does the output DATA look correct on sample rows?
- Each stage can fail independently. The agent must reflect on WHICH stage failed.
- Inner reflexion loop: fix the code (max 4 attempts)
- Outer loop: if fundamentally wrong approach after 4 inner attempts, try a different transformation strategy

This is Reflexion nested inside Plan-and-Execute (like Q17). How do you manage inner vs outer state? How does the reflection differ at each evaluation stage?

---

## MULTI-AGENT PATTERNS — Dedicated Questions

These questions test your understanding of **supervisor, orchestrator, swarm, and hierarchical** multi-agent patterns — when to use each, how to coordinate agents, and how to prevent common failure modes.

---

### Q29: Content Production Pipeline (Supervisor)
**Topics:** Supervisor pattern, worker agents, centralized delegation, context isolation

Design a content production system with a supervisor:
- **Supervisor**: receives a content brief, delegates to workers, reviews results
- **Researcher**: finds data, stats, and quotes for the article
- **Writer**: produces the article draft using research
- **Editor**: reviews the draft for grammar, clarity, and accuracy
- The supervisor can send the draft BACK to the writer with editor feedback (review loop, max 2 rounds)
- Each worker should only see the context it needs (not the full conversation)

Draw the graph. How does the supervisor decide who to call next? How do you prevent the supervisor from becoming a bottleneck? What does context isolation look like per worker?

---

### Q30: Customer Service Swarm
**Topics:** Swarm pattern, handoffs, circular handoff prevention, escalation

Design a customer service system with NO central supervisor:
- **Triage agent**: initial classification, routes to specialist
- **Billing agent**: handles invoices, payments, refunds. Tools: `lookup_invoice`, `process_refund`
- **Technical agent**: handles bugs, setup. Tools: `search_docs`, `create_ticket`
- **Account agent**: handles profile changes, cancellations. Tools: `update_profile`, `cancel_account`
- Any agent can hand off to any other agent if the customer's issue changes mid-conversation
- If an agent has been handed off to 3+ times, escalate to a human

How do you implement handoffs as tools? How do you prevent billing → technical → billing loops? What does the state need to track? How does a new agent pick up the conversation context?

---

### Q31: Software Development Orchestrator
**Topics:** Orchestrator pattern, planning + delegation, replanning, subgraphs per worker

Design a software development system:
- **Orchestrator**: takes a feature request, creates a plan, assigns tasks
- **Architect**: designs the technical approach (returns a design doc)
- **Developer**: writes code based on the design
- **Tester**: writes and runs tests for the code
- **Reviewer**: reviews code quality, can reject and send back to developer

The orchestrator plans upfront: design → develop → test → review.
BUT: if the tester finds a critical bug, the orchestrator should REPLAN (maybe redesign, not just patch).
Each worker can be a ReAct subgraph with its own tools.

How does the orchestrator decide when to replan vs just retry? How is this different from a plain supervisor? What does each worker's tool set look like?

---

### Q32: E-Commerce Support Hierarchy (Supervisor of Supervisors)
**Topics:** Hierarchical multi-agent, nested supervisors, subgraphs, cross-team escalation

Design a large e-commerce support system with 3 teams:
- **Order Team** (supervisor + workers): order_tracker, shipping_agent, returns_agent
- **Payment Team** (supervisor + workers): billing_agent, fraud_agent, refund_agent
- **Product Team** (supervisor + workers): catalog_agent, recommendation_agent

Top-level routing: a **CEO agent** routes to the right team supervisor.
Each team supervisor manages its own workers.

Challenges:
- Customer says "I was charged twice for an order that hasn't shipped" — this crosses Order Team AND Payment Team
- How do you handle cross-team issues?
- How deep can nesting go before it's too slow?
- When should a team supervisor escalate to the CEO vs handle locally?

---

### Q33: Research Debate System (Adversarial Multi-Agent)
**Topics:** Multi-agent debate, adversarial collaboration, judge agent, consensus building

Design a system where agents ARGUE to find the best answer:
- User asks a complex question (e.g., "Should we migrate from monolith to microservices?")
- **Advocate agent**: argues FOR microservices
- **Critic agent**: argues AGAINST microservices
- They go back-and-forth for 3 rounds, each seeing the other's arguments
- A **Judge agent** reads the full debate and produces a balanced recommendation

How does state flow between advocate and critic? How do you prevent the debate from going in circles? How does the judge weigh arguments? When is adversarial multi-agent better than a single agent?

---

### Q34: Autonomous Data Analytics Team (Mixed Patterns)
**Topics:** Combining supervisor + swarm + ReAct, dynamic agent creation, shared knowledge base

Design a data analytics system:
- **PM Agent** (orchestrator): takes a business question, plans the analysis, assigns tasks
- **SQL Agent** (ReAct): queries databases
- **Viz Agent** (ReAct): creates charts from data
- **Insight Agent**: interprets results and writes findings
- **Reviewer Agent**: validates statistical claims, checks for errors

Special requirements:
- The SQL agent might discover that the needed data is in a different database → it should hand off to a second SQL agent configured for that DB (swarm-like)
- The Viz agent can request more data from the SQL agent directly (not through PM) — peer-to-peer
- The PM coordinates the overall flow, but agents can talk to each other for small requests

This mixes orchestrator (PM plans), swarm (agents hand off), and ReAct (individual agents). How do you draw this graph? Where do you draw the line between "go through PM" vs "talk directly"?

---

## Topic Coverage Matrix

| Topic                          | Questions                              |
|--------------------------------|----------------------------------------|
| Nodes & Edges                  | Q1, Q2, Q4                             |
| Conditional Routing            | Q1, Q3, Q6, Q11                        |
| State Design                   | All                                    |
| Jinja Templates                | Q1, Q2, Q3, Q4, Q15                   |
| Structured Output (Pydantic)   | Q3, Q5, Q13, Q25                       |
| Checkpointing & Persistence    | Q7, Q9, Q14, Q16                      |
| Human-in-the-Loop              | Q7, Q10, Q21                           |
| Streaming                      | Q9, Q14                                |
| Tool Use                       | Q6, Q13, Q19-Q24                       |
| Cycles & Loops                 | Q6, Q12, Q13, Q17, Q19-Q28            |
| Parallel Execution             | Q8, Q18                                |
| Subgraphs                      | Q10, Q17, Q28, Q31, Q32               |
| Error Handling & Retries       | Q11, Q17, Q20                          |
| Production / Scale             | Q14, Q16                               |
| Dynamic Graphs                 | Q15                                    |
| Multi-Agent (original)         | Q12, Q18                               |
| **ReAct Pattern**              | **Q6, Q19, Q20, Q21, Q22, Q23, Q24**  |
| **Reflexion Pattern**          | **Q17, Q25, Q26, Q27, Q28**           |
| **Supervisor**                 | **Q29, Q32, Q34**                      |
| **Orchestrator**               | **Q31, Q34**                           |
| **Swarm**                      | **Q30, Q34**                           |
| **Hierarchical**               | **Q32**                                |
| **Adversarial / Debate**       | **Q33**                                |
