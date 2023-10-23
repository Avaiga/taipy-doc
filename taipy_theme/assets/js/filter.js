// Get all the filter filters and the list items
const filters = document.querySelectorAll('.tp-pills-filter input');
const listItems = document.querySelectorAll('.tp-filtered li');
let activeFilters = [];

// Attach event listeners to the filters
filters.forEach(checkbox => {
  checkbox.addEventListener('change', filterItems);
});

function handleAll(callback) {
  const newFilters = Array.from(filters)
    .filter(checkbox => checkbox.checked)
    .map(checkbox => checkbox.value);

  // If "all" is checked
  if ( newFilters.includes('all') ) {
      filters.forEach(checkbox => {
        const isFilterAll = checkbox.value === 'all';
        if (
          ( !activeFilters.includes('all') && !isFilterAll ) 
          || ( activeFilters.includes('all') && isFilterAll )
        ) {
          // If "all" wasn't checked before and gets checked, then uncheck every other filter    
          // OR If "all" was checked and another filter is checked, uncheck "all"
          checkbox.checked = false;
        }
      });
  } 
  else {
    // If no other checkbox is checked, check the "all" checkbox
    const otherFiltersChecked = newFilters.length > 0;
    document.getElementById('filter-all').checked = !otherFiltersChecked;
    // If every other is checked, just check "All" instead
    if (newFilters.length === filters.length - 1 ){
      filters.forEach(checkbox => {
        const isFilterAll = checkbox.value === 'all';
        checkbox.checked = isFilterAll;
      });  
    }
  }

  callback();
}

function applyFilters() {
  activeFilters = Array.from(filters)
    .filter(checkbox => checkbox.checked)
    .map(checkbox => checkbox.value);

  listItems.forEach(item => {
    let itemKeywords = [];
    if ( item.hasAttribute('data-keywords') ){
      itemKeywords = item.getAttribute('data-keywords').split(' ');
    }
    const shouldBeDisplayed = activeFilters.includes('all') || itemKeywords.some(keyword => activeFilters.includes(keyword));
    item.classList.toggle('is-hidden', !shouldBeDisplayed);
  });
}

function filterItems(){
  console.log('change');
  handleAll(applyFilters);
};

// Initially, call the filterItems function to show items based on the default checked filters
filterItems();