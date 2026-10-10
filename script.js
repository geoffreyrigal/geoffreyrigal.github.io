async function charge_file() { // Déclare une fonction asynchrone pour charger le contenu d'un fichier.
    const answer = await fetch("content/content.json"); // Demande index.html au serveur et attend la réponse.
    const text = await answer.json(); // Lit le corps de la réponse en supposant qu'il contient du JSON.
    return text;
}

async function inject_project(content, project) {
    content.querySelector(".content-title").textContent = project.title;
    content.querySelector(".content-date").textContent = project.date;
    content.querySelector(".content-language-title").textContent = "Langage utilisé(s) : ";
    content.querySelector(".content-language").textContent = project.languages.join(", ");
    content.querySelector(".content-techno-title").textContent = "Technologies utilisé(s) : ";
    content.querySelector(".content-techno").textContent = project.techno.join(", ");
    content.querySelector(".content-usage-title").textContent = "Role du projet";
    content.querySelector(".content-usage").textContent = project.usage;
    content.querySelector(".content-description-title").textContent = "Description du projet";
    content.querySelector(".content-description").textContent = project.description;
    const image = content.querySelector(".content-image");
    image.src = project.link_img;
    image.alt = project.alt_img;
}

async function main() {
    const projects = await charge_file();
    const content = document.querySelector(".project-content");
    const liste = document.querySelector(".project-menu ul");

    const already_in_list = [];

    projects.forEach((project, index) => {
        if (!already_in_list.includes(project.category)) {
            already_in_list.push(project.category);
            const ul = document.createElement("ul");
        }

        const li = document.createElement("li");
        li.textContent = project.title_menu;
        li.addEventListener("click", () => {
            inject_project(content, projects[index]);
        });
        liste.appendChild(li);
    });

    console.log(already_in_list.join());
}
main();