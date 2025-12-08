
interface Nail {
    name: string;
    description: string;
}

async function loadNailData(): Promise<Nail[]> {
    const response: Response = await fetch('/api/nails');
    const data: Nail[] = await response.json();
    
    // Get the element where you want to display the data
    const container: HTMLElement | null = document.getElementById('nail-data');
    if (container) {
        container.innerHTML = data.map((nail: Nail) => 
            `<div class='nail-item'>
                <h3>${nail.name}</h3>
                <p>${nail.description}</p>
            </div>`
        ).join('');    
    }
    
    return data;
}

function initializeApp() {
    // Attach button listeners
    const buttons = {
        'load-button': loadNailData
    };

    for (const [id, func] of Object.entries(buttons)) {
        document.getElementById(id)?.addEventListener('click', func);
    }
    
}

// Run initialization when script loads
initializeApp();

