let lineChart, pieChart;

document.addEventListener('DOMContentLoaded', function() {
    // Fetch asset classes and populate dropdown
    fetch('/api/asset-classes/')
        .then(response => response.json())
        .then(data => {
            const assetSelect = document.getElementById('asset-classes');
            data.forEach(asset => {
                const option = document.createElement('option');
                option.value = asset.name;
                option.textContent = asset.name;
                assetSelect.appendChild(option);
            });
        });

    // Initialize charts
    const lineCtx = document.getElementById('lineChart').getContext('2d');
    lineChart = new Chart(lineCtx, {
        type: 'line',
        data: { labels: [], datasets: [] },
        options: { responsive: true }
    });

    const pieCtx = document.getElementById('pieChart').getContext('2d');
    pieChart = new Chart(pieCtx, {
        type: 'pie',
        data: { labels: [], datasets: [{ data: [] }] },
        options: { responsive: true }
    });
});

function updateDashboard() {
    const granularity = document.getElementById('granularity').value;
    const startDate = document.getElementById('start-date').value;
    const endDate = document.getElementById('end-date').value;
    const assetClasses = Array.from(document.getElementById('asset-classes').selectedOptions).map(option => option.value);

    const url = `/api/financial-data/?granularity=${granularity}&start_date=${startDate}&end_date=${endDate}&asset_classes=${assetClasses.join(',')}`;

    fetch(url)
        .then(response => response.json())
        .then(data => {
            updateLineChart(data);
            updatePieChart(data);
            updateTable(data);
        });
}

function updateLineChart(data) {
    const labels = data.map(item => item.date);
    const datasets = Object.keys(data[0]).filter(key => key !== 'date').map(key => ({
        label: key,
        data: data.map(item => item[key]),
        borderColor: getRandomColor(),
        fill: false
    }));

    lineChart.data.labels = labels;
    lineChart.data.datasets = datasets;
    lineChart.update();
}

function updatePieChart(data) {
    if (data.length > 0) {
        const latestData = data[data.length - 1];
        const labels = Object.keys(latestData).filter(key => key !== 'date');
        const values = labels.map(label => latestData[label]);

        pieChart.data.labels = labels;
        pieChart.data.datasets[0].data = values;
        pieChart.update();
    }
}

function updateTable(data) {
    const table = document.getElementById('dataTable');
    table.innerHTML = '';  // Clear existing content

    if (data.length > 0) {
        const headers = ['Date', ...Object.keys(data[0]).filter(key => key !== 'date')];
        const thead = document.createElement('thead');
        const tr = document.createElement('tr');
        headers.forEach(header => {
            const th = document.createElement('th');
            th.textContent = header;
            tr.appendChild(th);
        });
        thead.appendChild(tr);
        table.appendChild(thead);

        const tbody = document.createElement('tbody');
        data.forEach(item => {
            const tr = document.createElement('tr');
            headers.forEach(header => {
                const td = document.createElement('td');
                td.textContent = item[header];
                tr.appendChild(td);
            });
            tbody.appendChild(tr);
        });
        table.appendChild(tbody);
    }
}

function getRandomColor() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}