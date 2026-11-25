// ======================================
// SEARCH + FILTER
// ======================================

const searchInput =
    document.getElementById("searchInput");

const statusFilter =
    document.getElementById("statusFilter");

const priorityFilter =
    document.getElementById("priorityFilter");

const sortFilter =
    document.getElementById("sortFilter");


function filterTasks() {

    const search =
        searchInput
            ? searchInput.value.toLowerCase()
            : "";

    const status =
        statusFilter
            ? statusFilter.value
            : "all";

    const priority =
        priorityFilter
            ? priorityFilter.value
            : "all";


    const cards =
        document.querySelectorAll(
            ".task-card"
        );


    cards.forEach(card => {

        const title =
            card.dataset.title;

        const description =
            card.dataset.description;

        const completed =
            card.dataset.completed === "true";

        const due =
            card.dataset.due;

        const cardPriority =
            card.dataset.priority;


        // Search

        const matchesSearch =
            title.includes(search) ||
            description.includes(search);


        // Status

        let matchesStatus = true;


        if (status === "pending") {

            matchesStatus =
                !completed;

        }


        if (status === "completed") {

            matchesStatus =
                completed;

        }


        if (status === "overdue") {

            matchesStatus =
                due === "overdue";

        }


        // Priority

        const matchesPriority =
            priority === "all" ||
            cardPriority === priority;


        if (
            matchesSearch &&
            matchesStatus &&
            matchesPriority
        ) {

            card.style.display =
                "block";

        } else {

            card.style.display =
                "none";

        }

    });

}


if (searchInput) {

    searchInput.addEventListener(
        "input",
        filterTasks
    );

}


if (statusFilter) {

    statusFilter.addEventListener(
        "change",
        filterTasks
    );

}


if (priorityFilter) {

    priorityFilter.addEventListener(
        "change",
        filterTasks
    );

}


// ======================================
// SORTING
// ======================================

if (sortFilter) {

    sortFilter.addEventListener(
        "change",
        function () {

            const value =
                this.value;

            const lists =
                document.querySelectorAll(
                    ".task-list"
                );


            lists.forEach(list => {

                const cards =
                    Array.from(
                        list.querySelectorAll(
                            ".task-card"
                        )
                    );


                cards.sort(
                    (a, b) => {

                        if (
                            value === "priority"
                        ) {

                            const order = {

                                High: 1,
                                Medium: 2,
                                Low: 3

                            };

                            return (
                                order[
                                    a.dataset.priority
                                ] -
                                order[
                                    b.dataset.priority
                                ]
                            );

                        }


                        if (
                            value === "due"
                        ) {

                            return (
                                getDueDate(a) -
                                getDueDate(b)
                            );

                        }


                        // Default
                        // newest/oldest

                        return 0;

                    }
                );


                if (
                    value === "oldest"
                ) {

                    cards.reverse();

                }


                cards.forEach(card => {

                    list.appendChild(card);

                });

            });

        }
    );

}


// ======================================
// GET DUE DATE
// ======================================

function getDueDate(card) {

    const text =
        card.querySelector(".due");

    if (!text) {

        return Infinity;

    }

    const match =
        text.textContent.match(
            /\d{1,2}\/\d{1,2}\/\d{4}/
        );


    if (!match) {

        return Infinity;

    }


    return new Date(
        match[0]
    );

}


// ======================================
// DARK MODE
// ======================================

function toggleDarkMode() {

    document.body.classList.toggle(
        "dark-mode"
    );


    const isDark =
        document.body.classList.contains(
            "dark-mode"
        );


    localStorage.setItem(
        "darkMode",
        isDark
    );

}


// Restore dark mode

if (
    localStorage.getItem(
        "darkMode"
    ) === "true"
) {

    document.body.classList.add(
        "dark-mode"
    );

}