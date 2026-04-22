async function loadMarketData() {
    const ticker = document.getElementById("marketTicker");

    try {
        const res = await fetch("/api/market");
        const data = await res.json();

        const USD_TO_INR = 83;

        const crudeINR = (data.crude_price * USD_TO_INR).toFixed(2);
        const gasINR = (data.gas_price * USD_TO_INR).toFixed(2);

        const crudeUp = data.crude_change >= 0;
        const gasUp = data.gas_change >= 0;

        ticker.innerHTML = `
            CRUDE OIL ₹${crudeINR}
            <span class="${crudeUp ? 'up' : 'down'}">
                (${crudeUp ? '▲' : '▼'} ${Math.abs(data.crude_change).toFixed(2)})
            </span>
            &nbsp; | &nbsp;
            NATURAL GAS ₹${gasINR}
            <span class="${gasUp ? 'up' : 'down'}">
                (${gasUp ? '▲' : '▼'} ${Math.abs(data.gas_change).toFixed(3)})
            </span>
        `;

    } catch (err) {
        ticker.innerHTML = "Market unavailable";
    }
}

loadMarketData();
setInterval(loadMarketData, 60000);