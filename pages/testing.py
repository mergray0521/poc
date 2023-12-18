import streamlit as st
import streamlit.components.v1 as com

with open("style.css") as source:
    design= source.read()

com.html(f"""
<div>
<style>
{design}
</style>
<h1 class="heading">
This is my heading
</h1>
<p>
paragraph lalalla
</p>
</div>
""", height=600)
