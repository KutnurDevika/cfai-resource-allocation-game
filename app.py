import streamlit as st
from dataclasses import dataclass
from collections import deque
import heapq

st.set_page_config(page_title="Competitive Resource Allocation Game", layout="wide")

# CO1
@dataclass
class State:
    military:int
    economy:int
    technology:int
    healthcare:int

class PEAS:
    performance = "Maximum Score"
    environment = "Competitive Environment"
    actuators = "Resource Allocation"
    sensors = "Opponent Data and Scores"

# CO2
class SearchAlgorithms:
    def bfs(self, graph, start):
        visited = []
        queue = deque([start])
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.append(node)
                for n in graph[node]:
                    queue.append(n)
        return visited

    def dfs(self, graph, start, visited=None):
        if visited is None:
            visited = []
        visited.append(start)
        for n in graph[start]:
            if n not in visited:
                self.dfs(graph, n, visited)
        return visited

    def ucs(self, graph, start, goal):
        pq = [(0, start)]
        visited = set()
        while pq:
            cost, node = heapq.heappop(pq)
            if node == goal:
                return cost
            if node not in visited:
                visited.add(node)
                for nbr, wt in graph[node]:
                    heapq.heappush(pq, (cost + wt, nbr))
        return None

# CO3
class CSPValidator:
    def validate(self, allocations):
        return sum(allocations.values()) <= 100

# CO4
class UtilityFunction:
    def calculate(self, allocations):
        return round(
            allocations["Military"] * 0.4 +
            allocations["Economy"] * 0.3 +
            allocations["Technology"] * 0.2 +
            allocations["Healthcare"] * 0.1, 2
        )

# CO5
class BayesianReasoning:
    def bayes_rule(self, prior, likelihood, evidence):
        return round((prior * likelihood) / evidence, 2)

search = SearchAlgorithms()
csp = CSPValidator()
utility_fn = UtilityFunction()
bayes = BayesianReasoning()

st.title("🎯 Competitive Resource Allocation Game")
st.write("AI Powered Strategic Decision Support System")

st.header("Resource Allocation")

military = st.slider("Military", 0, 100, 25)
economy = st.slider("Economy", 0, 100, 25)
technology = st.slider("Technology", 0, 100, 25)
healthcare = st.slider("Healthcare", 0, 100, 25)

allocations = {
    "Military": military,
    "Economy": economy,
    "Technology": technology,
    "Healthcare": healthcare
}

st.write(f"Total Allocation: {sum(allocations.values())}/100")

if st.button("Analyze Strategy"):
    if not csp.validate(allocations):
        st.error("Constraint Failed: Total allocation exceeds 100")
    else:
        st.success("CSP Validation Passed")

        state = State(military, economy, technology, healthcare)

        computer = {
            "Military": 25,
            "Economy": 25,
            "Technology": 25,
            "Healthcare": 25
        }

        utility_player = utility_fn.calculate(allocations)
        utility_computer = utility_fn.calculate(computer)

        rows = []
        player_score = 0
        computer_score = 0

        for sector in allocations:
            if allocations[sector] > computer[sector]:
                winner = "Player"
                player_score += 10
            elif allocations[sector] < computer[sector]:
                winner = "Computer"
                computer_score += 10
            else:
                winner = "Draw"

            rows.append({
                "Sector": sector,
                "Player": allocations[sector],
                "Computer": computer[sector],
                "Winner": winner
            })

        st.subheader("Battle Results")
        st.table(rows)

        c1, c2 = st.columns(2)
        c1.metric("Player Score", player_score)
        c2.metric("Computer Score", computer_score)

        st.subheader("CO4 - Utility Function")
        st.write("Player Utility:", utility_player)
        st.write("Computer Utility:", utility_computer)

        st.subheader("CO5 - Bayesian Analysis")
        posterior = bayes.bayes_rule(0.6, 0.7, 0.8)
        st.write("Posterior Probability:", posterior)

        st.subheader("CO6 - Hybrid AI Recommendation")
        if utility_player > utility_computer:
            st.success("Recommended Strategy: Continue Current Allocation")
        else:
            st.warning("Recommended Strategy: Increase Economy and Technology")

        if player_score > computer_score:
            st.success("🏆 Player Wins")
        elif computer_score > player_score:
            st.error("🤖 Computer Wins")
        else:
            st.info("Match Draw")

with st.expander("Advanced AI Features (CO1 & CO2)"):
    st.subheader("CO1 - PEAS Model")
    st.write("Performance:", PEAS.performance)
    st.write("Environment:", PEAS.environment)
    st.write("Actuators:", PEAS.actuators)
    st.write("Sensors:", PEAS.sensors)

    st.subheader("State Representation")
    st.write(State(military, economy, technology, healthcare))

    graph = {
        "A":["B","C"],
        "B":["D","E"],
        "C":["F"],
        "D":[],"E":[],"F":[]
    }

    wgraph = {
        "A":[("B",1),("C",4)],
        "B":[("D",2)],
        "C":[("D",1)],
        "D":[]
    }

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Run BFS"):
            st.write(search.bfs(graph, "A"))

    with col2:
        if st.button("Run DFS"):
            st.write(search.dfs(graph, "A"))

    with col3:
        if st.button("Run UCS"):
            st.write("Minimum Cost:", search.ucs(wgraph, "A", "D"))

         
