class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int :type trust: List[List[int]] :rtype: int

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

        # d is a function such that: i -> [out-degree, in-degree] i: person's label element [1,3] of trust can be
        # translated into   i) 1's out-degree increased by 1, ii) 3's in-degree increased by 1 a judge needs to have
        # 0 out-degree and n-1 in-degree and a judge is only one person

        # example)
        # trust = [[1,3],[2,3],[3,1]], n = 3
        # d = {1:[1,1], 2:[1,0], 3:[1,2]} => no [0,3] in d => no judge exist

        if len(trust) < n - 1: return -1

        judge = -1

        mutual = {i: [0, 0] for i in range(1, n + 1)}

        for pa, pb in trust:
            mutual[pa][0] += 1  # person_a trusting person_b stored as [0] component
            mutual[pb][1] += 1  # person_b trusted by person_a stored as [0] component

        for k, v in lookup.items():

            if v == [0, n - 1]:
                judge = k

        return judge
