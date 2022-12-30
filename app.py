import streamlit as st
import streamlit.components.v1 as components

components.html(
"""
<link rel="stylesheet" href="css/chessboard-1.0.0.min.css">
<script src="https://code.jquery.com/jquery-1.12.4.min.js"></script>
<script src="js/chessboard-1.0.0.min.js"></script>

<div id="board" style="width: 300px"></div>

<script>
    var board = ChessBoard('board', 'start');
</script>
""", height=300)
