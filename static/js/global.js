document.addEventListener("DOMContentLoaded", function () {

    /* ================= SLIDER ================= */
    let index = 0;
    const slides = document.querySelector(".slides");
    const totalSlides = document.querySelectorAll(".slide").length;

    function showSlide() {
        slides.style.transform = `translateX(-${index * 100}%)`;
    }

    function nextSlide() {
        index = (index + 1) % totalSlides;
        showSlide();
    }

    function prevSlide() {
        index = (index - 1 + totalSlides) % totalSlides;
        showSlide();
    }

    /* AUTO SLIDE */
    setInterval(nextSlide, 5000);

    /* BUTTON EVENTS */
    document.querySelector(".next").addEventListener("click", nextSlide);
    document.querySelector(".prev").addEventListener("click", prevSlide);

    /* ================= PROFILE DATA ================= */
    const data = {
        chirag: {
            name: "Chirag Bhojak",
            role: "CEO & Managing Director of NPCPL",
            img: "/static/image/chirag.png",
            desc: "Chirag Bhojak leads NPCPL with a strong vision for growth, innovation, and excellence in industrial solutions. His expertise in corporate strategy, business development, and client engagement helps build long-term partnerships across India and international markets. Under his leadership, NPCPL continues to expand its global presence, delivering reliable, high-quality solutions while maintaining a strong reputation for professionalism and trust."
        },
        ashok: {
            name: "Ashok Vyas",
            role: "Managing Director",
            img: "/static/image/ashok.png",
            desc: "Ashok Vyas leads NPCPL with a strong focus on operational excellence, strategic growth, and consistent quality. As Director, he brings expertise in business management, process optimization, and organizational leadership. His ability to streamline operations ensures efficient and reliable project execution. Under his direction, NPCPL continues to strengthen its foundation and uphold high standards of professionalism and trust."
        },
        sudhir: {
            name: "Sudhir Kirshnan",
            role: "CMO",
            img: "/static/image/sudhir.png",
            desc: "Sudhir Krishanan leads NPCPL’s market strategy with a strong focus on growth, client acquisition, and brand expansion. He specializes in market analysis, business development, and customer relationship management. His proactive approach helps identify new opportunities and strengthen the company’s market presence. Under his leadership, NPCPL continues to build strong client networks and maintain a competitive edge with professionalism and reliability."
        }
    };

    /* ================= MODAL ================= */
    const modal = document.getElementById("profileModal");

    window.openProfile = function (id) {
        modal.classList.add("active");

        document.getElementById("profileName").innerText = data[id].name;
        document.getElementById("profileRole").innerText = data[id].role;
        document.getElementById("profileImg").src = data[id].img;
        document.getElementById("profileDesc").innerText = data[id].desc;
    };

    window.closeProfile = function () {
        modal.classList.remove("active");
    };

    /* CLICK OUTSIDE CLOSE */
    window.addEventListener("click", function (e) {
        if (e.target === modal) {
            modal.classList.remove("active");
        }
    });

});
/* ================= GALLERY DATA ================= */
const galleryData = [
   {
        img: "/static/image/foundercabin.jpeg",
        title: "Founder Cabin",
        desc: "A thoughtfully designed workspace reflecting leadership vision, strategic thinking, and executive decision-making."
    },
    {
        img: "/static/image/ceocabin.png",
        title: "CEO Cabin",
        desc: "Executive workspace designed for leadership, strategy, and decision-making."
    },
    {
        img: "/static/image/director.png",
        title: "Director Cabin",
        desc: "A professional environment tailored for planning, coordination, and high-level business management."
    },
    {
        img: "/static/image/waitting.png",
        title: "Reception Area",
        desc: "Our modern reception area welcomes clients with a professional and comfortable environment."
    },
        {
        img: "/static/image/office.png",
        title: "Office Workspace",
        desc: "Collaborative workspace designed to enhance productivity and teamwork."
    },
    {
        img: "/static/image/confernceroom.jpeg",
        title: "Conference Room",
        desc: "Fully equipped meeting room for discussions, planning, and presentations."
    },
    {
        img: "/static/image/ceo.png",
        title: "Leadership in Action",
        desc: "Our leadership team is actively managing operations and driving growth, showcasing the vision and dedication of our CEO at work."
    },
    {
        img: "/static/image/about_refinery.jpeg",
        title: "Manufacturing Plant",
        desc: "Advanced refinery setup ensuring high-quality production and safety standards."
    },
     {
        img: "/static/image/dispacthunit.jpg",
        title: "Dispatch Unit",
        desc: "Efficient dispatch operations ensuring timely delivery and smooth logistics management across all supply channels."
    },
    {
        img: "/static/image/oil_manafuctering.jpg",
        title: "Oil Manufacturing Unit",
        desc: "Advanced oil manufacturing facility designed for precision processing and high-quality production standards."
    },
    {
        img: "/static/image/storage_tank.jpg",
        title: "Storage Tank Facility",
        desc: "High-capacity storage tanks built with safety compliance to securely store petrochemical products."
    },
    {
        img: "/static/image/solventstorage.jpg",
        title: "Solvent Storage Area",
        desc: "Dedicated solvent storage infrastructure ensuring proper handling, segregation, and environmental safety."
    }
];

/* OPEN GALLERY */
window.openGallery = function(index) {
    const modal = document.getElementById("galleryModal");

    document.getElementById("galleryImg").src = galleryData[index].img;
    document.getElementById("galleryTitle").innerText = galleryData[index].title;
    document.getElementById("galleryDesc").innerText = galleryData[index].desc;

    modal.classList.add("active");
};

/* CLOSE GALLERY */
window.closeGallery = function() {
    document.getElementById("galleryModal").classList.remove("active");
};

/* CLICK OUTSIDE CLOSE */
window.addEventListener("click", function(e) {
    const modal = document.getElementById("galleryModal");
    if (e.target === modal) {
        modal.classList.remove("active");
    }
});