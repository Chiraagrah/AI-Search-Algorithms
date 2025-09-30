# 🔍 Search Algorithm Visualizations

This project demonstrates the working of classic search algorithms using clear visualizations.  

---

## 🌟 A* Algorithm
The **A*** algorithm combines the cost to reach a node and a heuristic estimate of the remaining cost.  
It guarantees the shortest path if the heuristic is admissible.  

<p align="center">
  <img src="https://github.com/user-attachments/assets/5664e272-4d33-42a9-9098-3c1b20379ea7" width="70%" alt="A* Algorithm Visualization"/>
</p>

---

## 🚀 Greedy Best First Search
Greedy Best First Search chooses the path that appears best at each step using only the heuristic.  
It’s fast but not always optimal.  

<p align="center">
  <img src="https://github.com/user-attachments/assets/d44d00b7-0486-44eb-aede-63a1f72fc406" width="70%" alt="Greedy Best First Search Visualization"/>
</p>

---

## 🌐 Breadth First Search (BFS)
BFS explores nodes **level by level**.  
It guarantees the shortest path in an unweighted graph.  

<p align="center">
  <img src="https://github.com/user-attachments/assets/db060353-f912-4efc-b932-ab1419e9fb27" width="70%" alt="Breadth First Search Visualization"/>
</p>

---

## 🌀 Depth First Search (DFS)
DFS explores as deep as possible before backtracking.  
It does not guarantee the shortest path but uses less memory than BFS.  

<p align="center">
  <img src="https://github.com/user-attachments/assets/21a4139c-f99f-44cd-8d25-bf442bf1c438" width="70%" alt="Depth First Search Visualization"/>
</p>

---

## 📊 Comparison
| Algorithm              | Complete? | Optimal? | Time Complexity | Space Complexity |
|------------------------|-----------|----------|-----------------|------------------|
| **A\***               | ✅ Yes    | ✅ Yes   | O(E) with good heuristic | O(V) |
| **Greedy Best First** | ❌ No     | ❌ No    | O(E)            | O(V) |
| **BFS**               | ✅ Yes    | ✅ Yes (unweighted) | O(V+E) | O(V) |
| **DFS**               | ✅ Yes    | ❌ No    | O(V+E)          | O(V) |

---

✨ Explore the power of different search algorithms in pathfinding and problem solving!


