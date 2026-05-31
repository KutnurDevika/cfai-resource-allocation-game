import streamlit as st

st.title("Competitive Resource Allocation Game")

st.write("Allocate your resources across 3 zones.")

total_resources = 100

p1_z1 = st.number_input("Player 1 - Zone 1", 0, total_resources, 0)
p1_z2 = st.number_input("Player 1 - Zone 2", 0, total_resources, 0)
p1_z3 = st.number_input("Player 1 - Zone 3", 0, total_resources, 0)

p2_z1 = st.number_input("Player 2 - Zone 1", 0, total_resources, 0)
p2_z2 = st.number_input("Player 2 - Zone 2", 0, total_resources, 0)
p2_z3 = st.number_input("Player 2 - Zone 3", 0, total_resources, 0)

if st.button("Play Game"):

    p1_total = p1_z1 + p1_z2 + p1_z3
    p2_total = p2_z1 + p2_z2 + p2_z3

    if p1_total > total_resources or p2_total > total_resources:
        st.error("A player exceeded the resource limit of 100.")
    else:
        p1_score = 0
        p2_score = 0

        zones = [
            (p1_z1, p2_z1),
            (p1_z2, p2_z2),
            (p1_z3, p2_z3)
        ]

        for p1, p2 in zones:
            if p1 > p2:
                p1_score += 1
            elif p2 > p1:
                p2_score += 1

        st.subheader("Results")
        st.write(f"Player 1 Score: {p1_score}")
        st.write(f"Player 2 Score: {p2_score}")

        if p1_score > p2_score:
            st.success("Player 1 Wins!")
        elif p2_score > p1_score:
            st.success("Player 2 Wins!")
        else:
            st.info("It's a Tie!")