document.getElementById("careerForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const form = this;
    const formData = new FormData(form);
    const submitBtn = form.querySelector("button");

    // 🔄 loading state
    submitBtn.disabled = true;
    submitBtn.innerText = "Submitting...";

    try {
        const response = await fetch("/career", {
            method: "POST",
            body: formData
        });

        const result = await response.json();   // ⭐ VERY IMPORTANT

        if (response.ok && result.status === "success") {

            document.getElementById("successPopup").style.display = "block";
            form.reset();

        } else {

            alert(result.message || "Something went wrong. Please try again.");

        }

    } catch (error) {

        console.error(error);
        alert("Server error. Please try later.");

    } finally {

        // 🔁 restore button
        submitBtn.disabled = false;
        submitBtn.innerText = "Submit Application";

    }
});

function closePopup() {
    document.getElementById("successPopup").style.display = "none";
}
