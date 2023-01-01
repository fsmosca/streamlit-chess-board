import streamlit as st
import streamlit.components.v1 as components
from st_bridge import bridge
from modules.chess import Chess
from modules.utility import EPDS, set_page
from modules.states import init_states


set_page(title='Chess', page_icon="♟️")
init_states()


def cb_next():
    st.session_state.next += 1


if __name__ == '__main__':

    tabs = st.tabs(['Puzzle', 'Settings'])

    with tabs[1]:
        cols = st.columns([1, 3])
        with cols[0]:
            # Use dynamic board width for mobile phone.
            st.number_input(
                'Board Width',
                min_value=200,
                max_value=500,
                value=400,
                step=50,
                key='board_width'
            )

    with tabs[0]:
        cols = st.columns([1, 1])

        with cols[0]:
            # Show chess board based from fen.
            if st.session_state.next >= len(EPDS):
                st.session_state.next = 0

            epd = EPDS[st.session_state.next]
            fen = f"{' '.join(epd.split()[0:4])} 0 1"
            st.session_state.curfen = fen
            bm = epd.split('bm ')[1][0:-1]
            puzzle = Chess(st.session_state.board_width, fen)
            components.html(
                puzzle.puzzle_board(),
                height=st.session_state.board_width + 75,
                scrolling=False
            )

        # Get the info from current board after the user made the move.
        # The data will return the move, fen and the pgn.
        # The move contains the from sq, to square, and others.
        data = bridge("my-bridge", default=None)

        if data is not None:
            if st.session_state.oldfen != st.session_state.curfen:
                data = None
        st.session_state.oldfen = st.session_state.curfen

        with cols[1]:
            st.button('Next Position', on_click=cb_next)
            if data is not None:
                user_move = data['move']['san']
                if bm == user_move:
                    st.success(f'Congratulations, your move {user_move}'
                               ' is correct!')
                else:
                    st.error(f'Sorry, your move {user_move} is incorrect!')

                with st.expander('Board and user move info'):
                    st.markdown(f'''
                    move:  
                    **{data["move"]}**
                    ''')

                    # st.markdown(f'''
                    # fen:  
                    # **{data["fen"]}**
                    # ''')

                    # st.markdown(f'''
                    # pgn:  
                    # <strong>{data["pgn"]}</strong>
                    # ''', unsafe_allow_html=True)
