import streamlit as st
from static.my_apps.random_walks.caltech_stochastic_sim import RandomWalk


def walk_data():
    if "n_events" not in st.session_state:
        st.session_state["n_events"] = ""
    if "n_simulations" not in st.session_state:
        st.session_state["n_simulations"] = ""

    if "initial_position" not in st.session_state:
        st.session_state["initial_position"] = ""
    if "init_a" not in st.session_state:
        st.session_state["init_a"] = ""
    if "init_b" not in st.session_state:
        st.session_state["init_b"] = ""

    if "single_boundary" not in st.session_state:
        st.session_state["single_boundary"] = ""
    if "symmetric_boundary" not in st.session_state:
        st.session_state["symmetric_boundary"] = ""
    if "lower_bound" not in st.session_state:
        st.session_state["lower_bound"] = ""
    if "upper_bound" not in st.session_state:
        st.session_state["upper_bound"] = ""

    st.slider(label="Probability value", min_value=0.00, max_value=1.00, step=0.01, key="p_value")

    n_events = st.empty()
    n_simulations = st.empty()

    conditions = st.segmented_control(label="Starting position",
                                      selection_mode="single",
                                      options=["Single", "Interval"],
                                      default="Single",
                                      key="initial_conditions")
    if conditions == "Single":
        single_init = st.empty()
    elif conditions == "Interval":
        coli_1, coli_2 = st.columns(2)
        with coli_1:
            i1 = st.empty()
        with coli_2:
            i2 = st.empty()

    boundaries = st.segmented_control(label="Boundaries",
                                      selection_mode="single",
                                      options=["None", "Single", "Non-Symmetric"],
                                      default="None",
                                      key="boundary")
    if boundaries == "Single":
        single_bound = st.empty()
        symmetric = st.empty()
    elif boundaries == "Non-Symmetric":
        colb_1, colb_2 = st.columns(2)
        with colb_1:
            lb = st.empty()
        with colb_2:
            ub = st.empty()

    button = st.button("Refresh")
    button_clicks = 0
    if button:
        button_clicks += 1

        n_events.text_input("Number of steps: ", key=f"n_events_{button_clicks}", value="")
        n_simulations.text_input("Number of simulations", key=f"n_simulations_{button_clicks}", value="")

        if conditions == "Single":
            single_init.text_input("Initial condition: ", key=f"initial_position_{button_clicks}", value="")
        elif conditions == "Interval":
            i1.text_input("Lower: ", key=f"init_a_{button_clicks}", value="")
            i2.text_input("Upper: ", key=f"init_b_{button_clicks}", value="")

        if boundaries == "Single":
            single_bound.text_input("Boundary: ", key=f"single_boundary_{button_clicks}", value="")
            symmetric.toggle(label="Symmetric", key=f"symmetric_boundary_{button_clicks}", value=True)
        elif boundaries == "Non-Symmetric":
            colb_1, colb_2 = st.columns(2)
            with colb_1:
                lb.text_input("Lower: ", key=f"lower_bound_{button_clicks}", value="")
            with colb_2:
                ub.text_input("Upper: ", key=f"upper_bound_{button_clicks}", value="")

    else:
        if "n_events_1" not in st.session_state:
            st.session_state["n_events_1"] = ""
        if "n_simulations_1" not in st.session_state:
            st.session_state["n_simulations_1"] = ""

        if "initial_position_1" not in st.session_state:
            st.session_state["initial_position_1"] = ""
        if "init_a_1" not in st.session_state:
            st.session_state["init_a_1"] = ""
        if "init_b_1" not in st.session_state:
            st.session_state["init_b_1"] = ""

        if "single_boundary_1" not in st.session_state:
            st.session_state["single_boundary_1"] = ""
        if "symmetric_boundary_1" not in st.session_state:
            st.session_state["symmetric_boundary_1"] = ""
        if "lower_bound_1" not in st.session_state:
            st.session_state["lower_bound_1"] = ""
        if "upper_bound_1" not in st.session_state:
            st.session_state["upper_bound_1"] = ""

        n_events.text_input("Number of steps: ", key="n_events", value=st.session_state.n_events_1)
        n_simulations.text_input("Number of simulations: ", key="n_simulations", value=st.session_state.n_simulations_1)

        if conditions == "Single":
            single_init.text_input("Initial condition: ", key=f"initial_position", value=st.session_state.initial_position_1)
        elif conditions == "Interval":
            i1.text_input("Lower: ", key=f"init_a", value=st.session_state.init_a_1)
            i2.text_input("Upper: ", key=f"init_b", value=st.session_state.init_b_1)

        if boundaries == "Single":
            single_bound.text_input("Boundary: ", key="single_boundary", value=st.session_state.single_boundary_1)
            symmetric.toggle(label="Symmetric", key="symmetric_boundary", value=st.session_state.symmetric_boundary_1)
        elif boundaries == "Non-Symmetric":
            colb_1, colb_2 = st.columns(2)
            with colb_1:
                lb.text_input("Lower: ", key="lower_bound", value=st.session_state.lower_bound_1)
            with colb_2:
                ub.text_input("Upper: ", key="upper_bound", value=st.session_state.upper_bound_1)


def reset_session_state():
    for key in st.session_state.keys():
        del st.session_state[key]


def calibrate_data():

    try:
        st.session_state["walk_API"]["p_value"] = st.session_state["p_value"]

        if st.session_state["n_events"] != "":
            st.session_state["walk_API"]["n_events"] = int(st.session_state["n_events"])
        else:
            st.session_state["walk_API"]["n_events"] = 100

        if st.session_state["n_simulations"] != "":
            st.session_state["walk_API"]["n_simulations"] = int(st.session_state["n_simulations"])
        else:
            st.session_state["walk_API"]["n_simulations"] = 100

        if st.session_state["initial_conditions"] == "Single" and st.session_state["initial_position"] != "":
            st.session_state["walk_API"]["initial_conditions"] = float(st.session_state["initial_position"])
        elif st.session_state["initial_conditions"] == "Interval" and st.session_state["init_a"] != "" and st.session_state["init_b"] != "":
            st.session_state["walk_API"]["initial_conditions"] = (float(st.session_state["init_a"]), float(st.session_state["init_b"]))
        else:
            st.session_state["walk_API"]["initial_conditions"] = 0

        if st.session_state["boundary"] == "None":
            st.session_state["walk_API"]["boundary"] = None
        elif st.session_state["boundary"] == "Single" and st.session_state["single_boundary"] != "":
            st.session_state["walk_API"]["boundary"] = (float(st.session_state["single_boundary"]), st.session_state["symmetric_boundary"])
        elif st.session_state["boundary"] == "Non-Symmetric" and st.session_state["lower_bound"] != "" and st.session_state["upper_bound"] != "":
            st.session_state["walk_API"]["boundary"] = (float(st.session_state["lower_bound"]), float(st.session_state["upper_bound"]))
        else:
            st.session_state["walk_API"]["boundary"] = None

        walk_dict = st.session_state["walk_API"]
        st.session_state["walk"] = RandomWalk(p_value=walk_dict["p_value"],
                                              n_events=walk_dict["n_events"],
                                              n_simulations=walk_dict["n_simulations"],
                                              initial_conditions=walk_dict["initial_conditions"],
                                              boundary=walk_dict["boundary"])

    except ValueError:
        st.info("Make sure that all lower bounds are less than upper bounds, and that values entered are integers or floats.")
        st.button("Back", on_click=reset_session_state)
    except KeyError:
        st.info("No values to update. Try entering some!")
        st.button("Back", on_click=reset_session_state)


def main():
    # Page construction
    st.set_page_config(layout="wide")

    if "walk_API" not in st.session_state:
        st.session_state["walk_API"] = {
            "p_value": 0.5,
            "n_events": 100,
            "n_simulations": 100,
            "initial_conditions": 0,
            "boundary": None,
        }

    if "show_mean" not in st.session_state:
        st.session_state["show_mean"] = False

    if "walk" not in st.session_state:
        st.session_state["walk"] = RandomWalk(p_value=0.5,
                                              n_events=100,
                                              n_simulations=100,
                                              initial_conditions=0,
                                              boundary=None)

    col1, col2 = st.columns(2)

    with col1:
        walk_data()

    walk = st.session_state["walk"]
    fig, ax = walk.plot_process(plot_mean_pos=st.session_state["show_mean"], return_obj=True)

    with col2.container():
        st.pyplot(fig=fig)
        buttons = st.columns(3)
        with buttons[0].container(horizontal_alignment="center", vertical_alignment="center"):
            st.toggle(label="Show mean", key="show_mean")
        with buttons[1].container(horizontal_alignment="center", vertical_alignment="center"):
            st.button(label="Update", on_click=calibrate_data)
        with buttons[2].container(horizontal_alignment="center", vertical_alignment="center"):
            st.button(label="Reset", on_click=reset_session_state)


if __name__ == "__main__":
    main()