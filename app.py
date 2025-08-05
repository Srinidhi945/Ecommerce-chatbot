from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import os
from ecommbot.retrieval_generation import generation
from ecommbot.ingest import ingestdata

from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
from ecommbot.retrieval_generation import generation
from ecommbot.ingest import ingestdata

app = Flask(__name__)
load_dotenv()

vstore = ingestdata("done")
chain_builder = generation(vstore)  # Get chain builder function

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    session_id = request.remote_addr  # Can be improved with real session management
    chain = chain_builder(session_id)
    #result = chain.invoke({"question": msg}, config={"configurable": {"session_id": session_id}})
    question_text = str(msg).strip()  # ✅ Just to be safe
    result = chain.invoke(
    {"question": question_text},
    config={"configurable": {"session_id": session_id}}
)

    print("Response:", result)
    return str(result)

if __name__ == "__main__":
    app.run(debug=True)

