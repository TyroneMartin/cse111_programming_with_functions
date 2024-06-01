const input = document.querySelector("#favchap");
const button = document.querySelector("button");
const list = document.querySelector("#list");
let el = document.getElementById("close-button");

button.addEventListener("click", () => {
    if (input.value !== "") {
        const li = document.createElement("li");
        const deleteButton = document.createElement("button");
        
        li.innerHTML = input.value;
        deleteButton.textContent = "❌";
       
        li.appendChild(deleteButton);
        list.appendChild(li);

        deleteButton.addEventListener("click", () => {
            list.removeChild(li);
            input.focus();
        });

        input.focus();
        input.value = "";
    }
    
    else {
        window.alert("Please enter a Book and a Chapter");
    }
    ;
});
