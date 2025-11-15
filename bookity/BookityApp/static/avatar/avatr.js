const partsCatalog = {
 
    boca: [
        'avatar/images/boca1.png',
        'avatar/images/boca2.png',
        'avatar/images/boca3.png',
        'avatar/images/boca4.png',
        'avatar/images/boca5.png',
        'avatar/images/boca6.png',
        'avatar/images/boca7.png'
    ],
    
    
    cara: [
        'avatar/images/cara1.png',
        'avatar/images/cara2.png',
        'avatar/images/cara3.png',
        'avatar/images/cara4.png',
        'avatar/images/cara5.png'
    ],
    
   
    ceja: [
        'avatar/images/ceja1.png',
        'avatar/images/ceja2.png',
        'avatar/images/ceja3.png',
        'avatar/images/ceja4.png'
    ],
    
   
    ropa: [
        'avatar/images/chaqueta1.png',
        'avatar/images/chaqueta2.png',
        'avatar/images/chaqueta3.png',
        'avatar/images/chaqueta4.png',
        'avatar/images/polera1.png',
        'avatar/images/polera2.png',
        'avatar/images/polera3.png',
        'avatar/images/polera4.png',

    ],

 
    pelo: [
        'avatar/images/chas1.png',
        'avatar/images/chas2.png',
        'avatar/images/chas3.png',
        'avatar/images/chas4.png',
        'avatar/images/chas5.png',
        'avatar/images/chas6.png'
    ],

   
    ojos: [
        'avatar/images/ojos1.png',
        'avatar/images/ojos2.png',
        'avatar/images/ojos3.png',
        'avatar/images/ojos4.png',
        'avatar/images/ojos5.png',
        'avatar/images/ojos6.png',
        'avatar/images/ojos7.png'
    ],

  
    oreja: [
        'avatar/images/oreja1.png',
        'avatar/images/oreja2.png',
        'avatar/images/oreja3.png',
        'avatar/images/oreja4.png'
    ],

   
    patilla: [
        'avatar/images/patilla1.png',
        'avatar/images/patilla2.png',
        'avatar/images/patilla3.png',
        'avatar/images/patilla4.png',
        'avatar/images/patilla5.png',
        'avatar/images/patilla6.png',
        'avatar/images/patilla7.png'
    ],

  
    peloatras: [
        'avatar/images/pelotras1.png',
        'avatar/images/pelotras2.png',
        'avatar/images/pelotras3.png',
        'avatar/images/pelotras4.png',
        'avatar/images/pelotras5.png',
        'avatar/images/pelotras6.png',
        'avatar/images/pelotras7.png'
    ],
    
 
    pelonuca: [
        'avatar/images/pelonuca1.png',
        'avatar/images/pelonuca2.png',
        'avatar/images/pelonuca3.png',
        'avatar/images/pelonuca4.png'
    ],

     back: [
        'avatar/images/back1.png',
    ],
    
     back2: [
        'avatar/images/back2.png',
        'avatar/images/back21.png',
     ] 
}

const currentPartIndex = {
    pelo: 0,
    ojos: 0,
    cuerpo: 0,
    boca: 0,
    cara: 0,
    ropa: 0,
    ceja: 0,
    oreja: 0,
    patilla: 0,
    peloatras: 0,
    pelonuca: 0,
    back: 0,
    back2: 0,
}



function changeLayer(partName, index) {
    const relativePath = partsCatalog[partName][index];
    const layerElement = document.getElementById(`layer-${partName}`);
    
    if (layerElement && relativePath) {
        // Asume que tu ruta estática es /static/ y la concatena.
        layerElement.src = `/static/${relativePath}`; 
    }
}

function navigatePart(partName, direction) {
    const catalog = partsCatalog[partName];
    if (!catalog) return;

    const maxIndex = catalog.length - 1;
    let currentIndex = currentPartIndex[partName];

    let newIndex = currentIndex + direction;

    if (newIndex > maxIndex) {
        newIndex = 0; 
    } else if (newIndex < 0) {
        newIndex = maxIndex; 
    }
    
    currentPartIndex[partName] = newIndex;
    changeLayer(partName, newIndex);
    
    
    const controlGroup = document.querySelector(`.control-group[data-part="${partName}"]`);
    if (controlGroup) {
        const displaySpan = controlGroup.querySelector('.current-index-display');
        if (displaySpan) {
             displaySpan.textContent = `${newIndex + 1} / ${catalog.length}`;
        }
    }
}

