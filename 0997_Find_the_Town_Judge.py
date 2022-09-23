class Solution(object):
    def findJudge(self, n, trust):
        """
        https://leetcode.com/problems/find-the-town-judge/

        In a town, there are n people labeled from 1 to n.
        There is a rumor that one of these people is secretly the town judge.

        If the town judge exists, then:

        1. The town judge trusts nobody.
        2. Everybody (except for the town judge) trusts the town judge.
        3. There is exactly one person that satisfies properties 1 and 2.
        4. You are given an array trust where trust[i] = [ai, bi] representing that
        the person labeled ai trusts the person labeled bi.

        Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

        Example 1:

        Input: n = 2, trust = [[1,2]]
        Output: 2
        Example 2:

        Input: n = 3, trust = [[1,3],[2,3]]
        Output: 3
        Example 3:

        Input: n = 3, trust = [[1,3],[2,3],[3,1]]
        Output: -1


        Constraints:

        1 <= n <= 1000
        0 <= trust.length <= 104
        trust[i].length == 2
        All the pairs of trust are unique.
        ai != bi
        1 <= ai, bi <= n

        https://www.youtube.com/watch?v=OVdeIkc6Zmk
        """

        if len(trust) < n - 1: return -1

        trusting, trusted = 0, 0
        confidence = {person: [trusting, trusted] for person in range(1, n + 1)}

        for giver, earner in trust:
            confidence[giver][0] += 1  # trusting degree of the giver
            confidence[earner][1] += 1  # trusted degree of the earner

        for person, [trusting, trusted] in confidence.items():

            if [trusting, trusted] == [0, n - 1]:
                return person

        return -1
