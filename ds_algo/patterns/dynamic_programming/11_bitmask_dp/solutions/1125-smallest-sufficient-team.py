"""
1125. Smallest Sufficient Team (Hard)
https://leetcode.com/problems/smallest-sufficient-team/

Pattern: 11 - Bitmask DP

Given a list of required skills and a list of people (each with a subset of
skills), find the smallest team whose combined skills cover all required skills.

Approach:
    Represent the full skill set as a bitmask.
    dp[mask] = smallest team (as a list) that covers exactly the skills in mask.
    Start with dp[0] = [].
    For each person, for each already-reachable mask, compute
    new_mask = mask | person_skills. Update dp[new_mask] if the new team is
    smaller.

Time:  O(2^m * n)  where m = len(req_skills), n = len(people)
Space: O(2^m)
"""

from typing import List


class Solution:
    def smallestSufficientTeam(
        self, req_skills: List[str], people: List[List[str]]
    ) -> List[int]:
        """Return indices of the smallest team covering all required skills."""
        skill_idx = {s: i for i, s in enumerate(req_skills)}
        m = len(req_skills)
        full = (1 << m) - 1

        # Precompute each person's skill bitmask
        person_masks = []
        for p_skills in people:
            mask = 0
            for s in p_skills:
                if s in skill_idx:
                    mask |= 1 << skill_idx[s]
            person_masks.append(mask)

        # dp[mask] = smallest team (list of indices) achieving that mask
        dp = {0: []}

        for i, p_mask in enumerate(person_masks):
            if p_mask == 0:
                continue
            # Iterate over a snapshot of current dp keys
            for prev_mask, team in list(dp.items()):
                new_mask = prev_mask | p_mask
                if new_mask not in dp or len(dp[new_mask]) > len(team) + 1:
                    dp[new_mask] = team + [i]

        return dp[full]


# ───────────────────────── tests ─────────────────────────

def test_example1():
    req = ["java", "nodejs", "reactjs"]
    people = [["java"], ["nodejs"], ["nodejs", "reactjs"]]
    res = Solution().smallestSufficientTeam(req, people)
    assert len(res) == 2
    # Verify coverage
    covered = set()
    for idx in res:
        covered.update(people[idx])
    assert covered >= set(req)

def test_example2():
    req = ["algorithms", "math", "java", "reactjs", "csharp", "aws"]
    people = [
        ["algorithms", "math", "java"],
        ["algorithms", "math", "reactjs"],
        ["java", "csharp", "aws"],
        ["reactjs", "csharp"],
        ["csharp", "math"],
        ["aws", "java"],
    ]
    res = Solution().smallestSufficientTeam(req, people)
    assert len(res) == 2
    covered = set()
    for idx in res:
        covered.update(people[idx])
    assert covered >= set(req)

def test_single_person_all_skills():
    req = ["a", "b"]
    people = [["a", "b"]]
    assert Solution().smallestSufficientTeam(req, people) == [0]

def test_everyone_needed():
    req = ["a", "b", "c"]
    people = [["a"], ["b"], ["c"]]
    res = Solution().smallestSufficientTeam(req, people)
    assert len(res) == 3


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
