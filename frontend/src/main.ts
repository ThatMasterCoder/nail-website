
interface Nail {
    id: number;
    name: string;
    description: string;
    design: string;
    colors: string[];
    image: string;
}

async function loadNailData(): Promise<Nail[]> {
    const response: Response = await fetch('/api/nails');
    const data: Nail[] = await response.json();
    
    // Get the element where you want to display the data
    const container: HTMLElement | null = document.getElementById('nail-data');
    if (container) {
        container.innerHTML = data.map((nail: Nail) => 
            `<div class='nail-item'>
                <img src="images/${nail.image}" alt="${nail.name}" class="nail-image">
                <h3>${nail.name}</h3>
                <div class="design">Design: ${nail.design}</div>
                <p>${nail.description}</p>
                <div class="color-palette">
                    ${nail.colors.map(color => 
                        `<div class="color-swatch" style="background-color: ${color};" title="${color}"></div>`
                    ).join('')}
                </div>
            </div>`
        ).join('');
        
        // Smooth scroll to gallery after loading
        document.getElementById('gallery')?.scrollIntoView({ behavior: 'smooth' });
    }
    
    return data;
}

function initializeApp() {
    // Auto-load gallery if on gallery page
    if (document.getElementById('nail-data')) {
        loadNailData();
    }
}

// Run initialization when script loads
initializeApp();

