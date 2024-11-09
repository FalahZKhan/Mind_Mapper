let parsedIntegers = [];

document.getElementById('fileInput').addEventListener('change', handleFileUpload);

function handleFileUpload(event) {
  const file = event.target.files[0];
  const reader = new FileReader();
  reader.onload = function(e) {
    const content = e.target.result;
    parseInput(content);
  };
  reader.readAsText(file);
}

function parseInput(content) {
  const values = content.trim().split(/\s+/).map(Number);
  if (values.length === 2) {
    parsedIntegers = values;
  } else {
    alert("Please upload a valid file with exactly two integers.");
  }
}

function multiplyIntegers() {
  if (parsedIntegers.length !== 2) {
    alert("Please upload a file with exactly two integers.");
    return;
  }
  const [x, y] = parsedIntegers;

  fetch('/api/integer-multiplication', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ x, y })
  })
  .then(response => response.json())
  .then(data => {
    if (data.error) {
      document.getElementById('result').innerHTML = `Error: ${data.error}`;
    } else {
      document.getElementById('result').innerHTML = `Result of Integer Multiplication: ${data.result}`;
      document.getElementById('timeComplexity').innerHTML = "Time Complexity: O(log n)";
      document.getElementById('spaceComplexity').innerHTML = "Space Complexity: O(log n)";
    }
  })
  .catch(error => console.error('Error:', error));
}
