async function loadFiles() {
    const r = await fetch("/files");
    const files = await r.json();

    const box = document.getElementById("files");

    if (!files.length) {
        box.innerHTML = "<p>Brak firmware.</p>";
        return;
    }

    box.innerHTML = "";

    files.forEach(file => {
        const row = document.createElement("div");

        row.innerHTML = `
            <b>${file.name}</b>
            (${file.size} B)
            <button onclick="flash('${file.name}')">Flash</button>
        `;

        box.appendChild(row);
    });
}

async function flash(filename) {
    const r = await fetch("/flash", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            filename,
            address: "0x0",
            baud: 460800
        })
    });

    const job = await r.json();

    alert("Flash rozpoczęty\nJob ID:\n" + job.job_id);
}

loadFiles();
