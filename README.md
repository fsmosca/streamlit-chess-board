# streamlit-chess-board

The app is powered by [chessboardjs](https://chessboardjs.com/), [chessjs](https://github.com/jhlywa/chess.js), and [streamlit-bridge](https://pypi.org/project/streamlit-bridge/). The streamlit-bridge is used to return the board update and move informations done by the user. Data such as move, fen and pgn are returned which can be use in the python code.

### Broken

This will only work when run locally with `streamlit run app.py`. But it will not work when deployed in streamlit cloud.

![image](https://user-images.githubusercontent.com/22366935/210167497-026a19ac-5936-4e0b-8242-447e28a645cb.png)

### UI when run locally

![image](https://user-images.githubusercontent.com/22366935/210167243-c6250a62-dd3a-497e-93b1-fad4d84ae627.png)


## Setup

* git clone https://github.com/fsmosca/streamlit-chess-board.git
* cd streamlit-chess-board
* pip install -r requirements.txt
* streamlit run app.py
