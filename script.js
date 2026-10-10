async function charge_file() {
    const answer = await fetch("content.json");
    const text = await answer.json();
    return text;
}

let currentImages = [];
let currentImageIndex = 0;
let currentAlt = "";

function updateCarrouselDisplay(content) {
    const carrousel = content.querySelector(".content-carrousel");
    if (!carrousel) return;

    if (currentImages.length === 0) {
        carrousel.style.display = "none";
        return;
    }

    carrousel.style.display = "flex";

    const image = carrousel.querySelector(".content-image");
    const prevBtn = carrousel.querySelector(".prev");
    const nextBtn = carrousel.querySelector(".next");

    image.src = currentImages[currentImageIndex];
    image.alt = currentAlt;

    let indicators = carrousel.querySelector(".carrousel-indicators");

    if (currentImages.length <= 1) {
        if (prevBtn) prevBtn.style.display = "none";
        if (nextBtn) nextBtn.style.display = "none";
        if (indicators) indicators.style.display = "none";
    } else {
        if (prevBtn) prevBtn.style.display = "flex";
        if (nextBtn) nextBtn.style.display = "flex";

        if (!indicators) {
            indicators = document.createElement("div");
            indicators.className = "carrousel-indicators";
            carrousel.appendChild(indicators);
        }
        indicators.style.display = "flex";
        indicators.innerHTML = "";

        currentImages.forEach((_, idx) => {
            const dot = document.createElement("button");
            dot.className = "carrousel-dot" + (idx === currentImageIndex ? " active" : "");
            dot.type = "button";
            dot.setAttribute("aria-label", `Afficher l'image ${idx + 1}`);
            dot.addEventListener("click", () => {
                currentImageIndex = idx;
                updateCarrouselDisplay(content);
            });
            indicators.appendChild(dot);
        });
    }
}

function initCarrousel(content) {
    const prevBtn = content.querySelector(".content-carrousel .prev");
    const nextBtn = content.querySelector(".content-carrousel .next");

    if (prevBtn) {
        prevBtn.addEventListener("click", () => {
            if (currentImages.length > 1) {
                currentImageIndex = (currentImageIndex - 1 + currentImages.length) % currentImages.length;
                updateCarrouselDisplay(content);
            }
        });
    }

    if (nextBtn) {
        nextBtn.addEventListener("click", () => {
            if (currentImages.length > 1) {
                currentImageIndex = (currentImageIndex + 1) % currentImages.length;
                updateCarrouselDisplay(content);
            }
        });
    }

    document.addEventListener("keydown", (e) => {
        if (currentImages.length > 1) {
            if (e.key === "ArrowLeft") {
                currentImageIndex = (currentImageIndex - 1 + currentImages.length) % currentImages.length;
                updateCarrouselDisplay(content);
            } else if (e.key === "ArrowRight") {
                currentImageIndex = (currentImageIndex + 1) % currentImages.length;
                updateCarrouselDisplay(content);
            }
        }
    });
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

    if (Array.isArray(project.link_img)) {
        currentImages = project.link_img;
    } else if (typeof project.link_img === "string" && project.link_img.trim() !== "") {
        currentImages = [project.link_img];
    } else {
        currentImages = [];
    }

    currentImageIndex = 0;
    currentAlt = project.alt_img || project.title || "Image du projet";
    updateCarrouselDisplay(content);
}

async function main() {
    const projects = await charge_file();
    const content = document.querySelector(".project-content");
    const liste = document.querySelector(".project-menu ul");

    initCarrousel(content);

    const categoryLists = {};

    projects.forEach((project) => {
        if (!categoryLists[project.category]) {
            const categoryLi = document.createElement("li");
            
            const categoryTitle = document.createElement("strong");
            categoryTitle.textContent = project.category;
            categoryLi.appendChild(categoryTitle);

            const subUl = document.createElement("ul");
            categoryLi.appendChild(subUl);

            liste.appendChild(categoryLi);

            categoryLists[project.category] = subUl;
        }

        const li = document.createElement("li");
        li.textContent = project.title_menu;
        li.classList.add("project-item");
        li.addEventListener("click", () => {
            document.querySelectorAll(".project-item").forEach((item) => item.classList.remove("active"));
            li.classList.add("active");

            inject_project(content, project);
        });

        categoryLists[project.category].appendChild(li);
    });
}
main();