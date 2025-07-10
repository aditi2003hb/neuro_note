async function generate() {
  const topic = document.getElementById("topic").value;
  const content = document.getElementById("content").value;

  const response = await fetch("http://localhost:8000/api/generate", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ topic, content })
  });

  const data = await response.json();

  const outputDiv = document.getElementById("output");
  outputDiv.innerHTML = `
    <h2>📝 Summary:</h2>
    <p>${data.summary}</p>

    <h2>📚 Flashcards:</h2>
    <ul>${data.flashcards.map(f => `<li>${f}</li>`).join("")}</ul>

    <h2>❓ Quiz Question:</h2>
    <p>${data.quiz}</p>
  `;
}
