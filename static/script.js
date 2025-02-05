function previewImage() {
    let input = document.getElementById("imageInput");
    let previewContainer = document.getElementById("preview-container");
    let previewImage = document.getElementById("previewImage");

    if (input.files && input.files[0]) {
        let reader = new FileReader();
        reader.onload = function (e) {
            previewImage.src = e.target.result;
            previewContainer.style.display = "block";
        };
        reader.readAsDataURL(input.files[0]);
    }
}

document.getElementById("uploadForm").addEventListener("submit", function (e) {
    e.preventDefault();

    let input = document.getElementById("imageInput");
    if (input.files.length === 0) {
        Swal.fire("Error", "Please select an image first!", "error");
        return;
    }

    let formData = new FormData();
    formData.append("image", input.files[0]);

    fetch("/predict", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            Swal.fire("Error", data.error, "error");
        } else {
            document.getElementById("result").style.display = "block";
            
            document.getElementById("category").innerText = data.category;
            document.getElementById("grade").innerText = data.grade;
            document.getElementById("accuracy").innerText = data.accuracy;
        }
    })
    .catch(error => {
        console.error("Error:", error);
        Swal.fire("Error", "Something went wrong!", "error");
    });
});
