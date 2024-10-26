document.addEventListener('DOMContentLoaded', function() {
    const percentageCircle = document.querySelector('.percentage-circle');
    if (percentageCircle) {
        const percentage = percentageCircle.dataset.percentage;
        const degrees = (percentage / 100) * 360;
        percentageCircle.style.background = `conic-gradient(
            #3498db ${degrees}deg,
            #e0e0e0 ${degrees}deg
        )`;
    }
});
