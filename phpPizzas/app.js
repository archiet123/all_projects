function onReady() {
    $(".orderOption *").each((index, element) => {
        $(element).on("click", (event) => {
            // Stop default actions (like page refresh)
            event.preventDefault();

            const from = $("#active");
            const to = $(element);

            // Remove attribute "id"
            // Setting the ID to an empty string works too
            from.attr("id", "");

            // Set the clicked element to have the id active
            to.attr("id", "active");

            const fromBoxName = from.attr("class");
            const toBoxName = to.attr("class");

            $(`.${fromBoxName}-container`).addClass("hidden");
            $(`.${toBoxName}-container`).removeClass("hidden");
        });
    });
}

$(document).ready(onReady);
