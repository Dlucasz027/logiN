tsParticles.load("particles-js", {
    particles: {
        number: {
            value: 60,
            density: {
                enable: true,
                value_area: 800
            }
        },
        color: {
            value: "#ffffff"
        },
        shape: {
            type: "circle",
        },
        opacity: {
            value: 0.7,
            random: true,
        },
        size: {
            value: 3,
            random: true,
        },
        line_linked: {
            enable: false,
        },
        move: {
            enable: true,
            speed: 0.8,
            direction: "none",
            random: true,
            straight: false,
            out_mode: "out",
            bounce: false,
        }
    },

    interactivity: {
        detect_on: "canvas",
        events: {
            onhover: {
                enable: false,
            },
            onclick: {
                enable: false,
            },
            resize: true
        }
    },
    retina_detect: true
});