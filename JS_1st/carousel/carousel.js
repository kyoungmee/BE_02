

const carousel = document.getElementById("carousel")
const prevBtn = document.getElementById("prev")
const nextBtn = document.getElementById("next")

console.log(carousel, prevBtn,nextBtn)

let index = 0;

prevBtn.addEventListener("click",()=>{
    if(index === 0) return;
        index -= 1;
        carousel.style.transform = `translate3d(-${400*index}px,0,0)`;
})

nextBtn.addEventListener("click",()=>{
    if(index === 2) return;
        index += 1;
        carousel.style.transform = `translate3d(-${400*index}px,0,0)`;
})