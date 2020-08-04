document.addEventListener('DOMContentLoaded', () => {

    let cheeseClicked = false;

    document.querySelectorAll('.cheese-check-input').forEach(function(button) {
        button.onclick = function() {

            if (cheeseClicked == false) {
                cheeseClicked = true;
            } else {
                cheeseClicked = false;
            };


            let dish = this.id;

            let matches = dish.match(/(\d+)/);
            let id = matches[0];

            let smallPrice = document.getElementById(`${id}-small-price-input`).name;
            let largePrice = document.getElementById(`${id}-large-price-input`).name;

            let newSmallPrice = (Number(smallPrice) + 0.5).toFixed(2);
            let newLargePrice = (Number(largePrice) + 0.5).toFixed(2);
            
            if (cheeseClicked == true) {
                document.getElementById(`${id}-small-price`).innerHTML = newSmallPrice;
                document.getElementById(`${id}-large-price`).innerHTML = newLargePrice;

                document.getElementById(`${id}-small-price-input`).setAttribute("name", newSmallPrice);
                document.getElementById(`${id}-large-price-input`).setAttribute("name", newLargePrice);

                document.getElementById(`${id}-add-small-sub`).setAttribute("name", "addsizeitemcheese");
                document.getElementById(`${id}-add-large-sub`).setAttribute("name", "addsizeitemcheese");
            } else {
                document.getElementById(`${id}-small-price`).innerHTML = (smallPrice - 0.5).toFixed(2);
                document.getElementById(`${id}-large-price`).innerHTML = (largePrice - 0.5).toFixed(2);
            
                document.getElementById(`${id}-small-price-input`).setAttribute("name", (smallPrice - 0.5).toFixed(2));
                document.getElementById(`${id}-large-price-input`).setAttribute("name", (largePrice - 0.5).toFixed(2));

                document.getElementById(`${id}-add-small-sub`).setAttribute("name", "addsizeitem");
                document.getElementById(`${id}-add-large-sub`).setAttribute("name", "addsizeitem");
            };

        };
    });


    let subToppingsClicked = 0;
    let chosenSubToppings = [];

    document.querySelectorAll('.topping-check-input').forEach(function(button) {
        button.onclick = function() {

            let dish = this.id;
            let topping = this.name;

            let matches = dish.match(/(\d+)/);
            let id = matches[0];

            let smallPrice = document.getElementById(`${id}-small-price-input`).name;
            let largePrice = document.getElementById(`${id}-large-price-input`).name;

            let newSmallPrice = (Number(smallPrice) + 0.5).toFixed(2);
            let newLargePrice = (Number(largePrice) + 0.5).toFixed(2);

            if (document.getElementById(`extra-${topping}-${id}`).checked) {
                subToppingsClicked += 1;
                chosenSubToppings.push(topping);

                document.getElementById(`${id}-small-price`).innerHTML = newSmallPrice;
                document.getElementById(`${id}-large-price`).innerHTML = newLargePrice;

                document.getElementById(`${id}-small-price-input`).setAttribute("name", newSmallPrice);
                document.getElementById(`${id}-large-price-input`).setAttribute("name", newLargePrice);

                let chosen = chosenSubToppings.join(" ");
                document.getElementById(`${id}-add-small-sub`).setAttribute("value", `${id} small ${subToppingsClicked} ${chosen}`);
                document.getElementById(`${id}-add-large-sub`).setAttribute("value", `${id} large ${subToppingsClicked} ${chosen}`);
            } else {
                subToppingsClicked -= 1;
                let index = chosenSubToppings.indexOf(topping);
                chosenSubToppings.splice(index, 1);

                document.getElementById(`${id}-small-price`).innerHTML = (smallPrice - 0.5).toFixed(2);
                document.getElementById(`${id}-large-price`).innerHTML = (largePrice - 0.5).toFixed(2);

                document.getElementById(`${id}-small-price-input`).setAttribute("name", (smallPrice - 0.5).toFixed(2));
                document.getElementById(`${id}-large-price-input`).setAttribute("name", (largePrice - 0.5).toFixed(2));

                let chosen = chosenSubToppings.join(" ");
                document.getElementById(`${id}-add-small-sub`).setAttribute("value", `${id} small ${subToppingsClicked} ${chosen}`);
                document.getElementById(`${id}-add-large-sub`).setAttribute("value", `${id} large ${subToppingsClicked} ${chosen}`);
            };
        };
    });



    document.querySelectorAll('.select-toppings').forEach(function(button) {
        button.onclick = function() {

            let pizza = this.id;
            console.log(`pizza id 1: ${pizza}`);

            if (document.getElementById(`regular-toppings-${pizza}`).style.display == 'none'){
                document.getElementById(`regular-toppings-${pizza}`).style.display = 'block';
            } else {
                document.getElementById(`regular-toppings-${pizza}`).style.display = 'none';

            };

        };
    });

    let toppingsClicked = 0;
    let chosenToppings = [];

    document.querySelectorAll('.toppings-check-input').forEach(function(button) {
        button.onclick = function() {

            let topping = this.name;
            let pizza = this.value;
            let pizza_id = this.id;
            let numbers = pizza_id.match(/(\d+)/);
            let id = numbers[0];
            console.log(`topping chosen: ${topping}`);
            console.log(`pizza chosen: ${pizza}`);
            console.log(`pizza id chosen: ${id}`);

            if (document.getElementById(`extra-${topping}-${id}`).checked) {
                toppingsClicked += 1;
                chosenToppings.push(topping);

                let chosen = chosenToppings.join(" ");
                document.getElementById(`${id}-add-small-reg`).setAttribute("value", `${id} small ${toppingsClicked} ${chosen}`);
                document.getElementById(`${id}-add-large-reg`).setAttribute("value", `${id} large ${toppingsClicked} ${chosen}`);
            } else {
                toppingsClicked -= 1;
                let index = chosenToppings.indexOf(topping);
                chosenToppings.splice(index, 1);
               let chosen = chosenToppings.join(" ");
                document.getElementById(`${id}-add-small-reg`).setAttribute("value", `${id} small ${toppingsClicked} ${chosen}`);
                document.getElementById(`${id}-add-large-reg`).setAttribute("value", `${id} large ${toppingsClicked} ${chosen}`);
            };

            let matches = pizza.match(/(\d+)/);
            let numOfTops = matches[0];
            console.log(numOfTops);

            let toppings = document.querySelectorAll('.toppings-check-input');

            if (toppingsClicked == numOfTops) {
                toppings.forEach(function(item) {
                    if (!chosenToppings.includes(item.name)) {
                        item.disabled = true;
                    };
                });
            } else {
                toppings.forEach(function(item) {
                    item.disabled = false;
                });
            };
        };
    });



});