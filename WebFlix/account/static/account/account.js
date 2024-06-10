document.querySelector(".popup").addEventListener("click", () => {
    document.querySelector(".modal").classList.add("open");
    document.querySelector(".modal_box").classList.add("open");
});
document.querySelector(".button-delete").addEventListener("click", () => {
    document.querySelector(".modal").classList.remove("open");
    document.querySelector(".modal_box").classList.remove("open");
});

const ctx = document.getElementById('myChart').getContext("2d");
var fantazy = document.getElementById("fantazy").value;
var dram = document.getElementById("dram").value;
var kriminal = document.getElementById("kriminal").value;
var science = document.getElementById("science").value;
var comedy = document.getElementById("comedy").value;
var horror = document.getElementById("horror").value;
var multfilm = document.getElementById("multfilm").value;

 let myChar =  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['fantazy', 'dram', 'kriminal', 'science', 'comedy', 'horror', 'multfilm'],
      datasets: [{
        label: 'View statistics',
        data: [fantazy, dram, kriminal, science, comedy, horror, multfilm],
        backgroundColor:[
            "#23ff00",
            "#8bff78",
            "#beffb4",
            "#e3ffde",
            "#23ff00",
            "#8bff78",
            "#fafff9"
        ],
        borderColor:[
        ],
        borderWidth: 2
      }]
    },
    options: {}
  });
