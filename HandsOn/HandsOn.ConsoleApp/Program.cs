﻿using System;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;

namespace HandsOn.ConsoleApp
{
    class Program
    {
        static void Main(string[] args)
        {
            // //Magic Value of an Array
            // var intArr = new List<int>{0, 2, 1, 4}; //, 1, 0, 3, 2, 1, 0, 4};

            // Dictionary<int, int> originalMap = new Dictionary<int, int>();
            // for(int i = 0; i < intArr.Count; i++)
            //     originalMap.Add(i, intArr[i]);
            
            // // Array.Sort(intArr);
            // intArr.Sort();

            // int goodInt = 0, badInt = 0;

            // for (int i = 0; i < intArr.Count; i++)
            // {
            //     int valueAtPosition = originalMap.GetValueOrDefault(i);
            //     // compare sorted array position
            //     if (valueAtPosition != intArr[i])
            //         badInt += 1;
            //     else
            //         goodInt += 1;
            // }

            // System.Console.WriteLine(goodInt - badInt);

            // Kruskal's MST
            Kruskals kmst = new Kruskals();
            kmst.FindMST(4, 5);

            CriticalConnections cc = new CriticalConnections();
            int n = 5;
            // int n = 9;

            IList<IList<int>> connections = new List<IList<int>>();
            connections.Add(new List<int> { 1, 2 });
            connections.Add(new List<int> { 3, 4 });
            connections.Add(new List<int> { 1, 3 });
            connections.Add(new List<int> { 1, 4 });
            connections.Add(new List<int> { 4, 5 });

            // connections= new List<IList<int>>{
            //     new List<int>{1, 2},
            //     new List<int>{1, 3},
            //     new List<int>{2, 3},
            //     new List<int>{3, 4},
            //     new List<int>{3, 6},
            //     new List<int>{4, 5},
            //     new List<int>{6, 7},
            //     new List<int>{6, 9},
            //     new List<int>{7, 8},
            //     new List<int>{8, 9}
            // };


            cc.GetCriticalConnections(n, connections);

            System.Console.WriteLine();

            var inputString = "hit";
            var targetString = "cog";

            IList<String> list = new List<String> { "hot", "dot", "dog", "lot", "log", "cog" };

            int expectedValue = 5;

            var actual_value = new WordLadder().FindMinLadder(inputString, targetString, list);

            Trace.Assert(actual_value == expectedValue, $"Returned value - {actual_value}");

            list = new List<String> { "hot", "dot", "dog", "lot", "log" };

            expectedValue = 0;
            actual_value = new WordLadder().FindMinLadder(inputString, targetString, list);

            Trace.Assert(actual_value == expectedValue, $"Returned value - {actual_value}");

            list = new List<String> { "hot", "dog", "dot" };

            inputString = "hot";
            targetString = "dog";
            expectedValue = 3;

            actual_value = new WordLadder().FindMinLadder(inputString, targetString, list);

            Trace.Assert(actual_value == expectedValue, $"Returned value - {actual_value}");

            int size = 5;

            var uf = new UnionFind(size);

            System.Console.WriteLine("Total sets :" + uf.getTotalSet());

            uf.union(0, 1);
            Trace.Assert(uf.getSetSize(0) == 2);

            uf.union(1, 0);
            Trace.Assert(uf.getSetSize(0) == 2);
            Trace.Assert(uf.getTotalSet() == 4);

            uf.union(1, 2);
            Trace.Assert(uf.getSetSize(0) == 3);
            Trace.Assert(uf.getSetSize(3) == 1);
            Trace.Assert(uf.getTotalSet() == 3);

            uf = new UnionFind(12);

            IEnumerable<Edge> edges = new List<Edge>{
                new Edge(1, 2),
                new Edge(1, 7),
                new Edge(1, 8),
                new Edge(2, 3),
                new Edge(2, 6),
                new Edge(3, 4),
                new Edge(3, 5),
                new Edge(8, 9),
                new Edge(8, 12),
                new Edge(9, 10),
                new Edge(9, 11),
                new Edge(11, 12)
            };

            Graph g = new Graph(edges);
            uf = new UnionFind(g.Vertices.Count);

            Trace.Assert(uf.FindCycle(g) == true);

            var obj = new Solution();

            int[] A = new int[] { 1, 4, 2 };
            int[] B = new int[] { 1, 2, 4 };

            int expectedOutput = 2;
            int actualOutput = obj.MaxUncrossedLines(A, B);

            Trace.Assert(actualOutput == expectedOutput);

            var mde = new MinimumEditDistance();
            var word_from = "horse";
            var word_to = "ros";

            expectedOutput = 3;
            actualOutput = mde.MinDistance(word_from, word_to);

            Trace.Assert(expectedOutput == actualOutput);

            String X = "ABCBDAB";
            String Y = "BDCABA";
            var lcs = new LCS();

            expectedOutput = 4;
            actualOutput = lcs.LongestCommonSubsequence(X, Y);

            Trace.Assert(actualOutput == expectedOutput);
        }
    }
}
