// Verhindert MS Teams Browser Tab Inaktivitätsanzeige
function simulateMouseMove() {
    var evt = new MouseEvent('mousemove', {
        bubbles: true,
        cancelable: true,
        view: window,
        clientX: 0,
        clientY: 0
    });
    window.dispatchEvent(evt);
}

// Bewege die Maus jede Minute
setInterval(simulateMouseMove, 60000);
