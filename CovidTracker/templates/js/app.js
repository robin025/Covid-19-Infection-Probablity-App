const searchinputbox = document.getElementById('inputsearch');
        searchinputbox.addEventListener('keypress', (event) => {
            if (event.keyCode == 13) {
                console.log(searchinputbox.value);
                getweatherreport(searchinputbox.value);

            }

        });


        // getweatherreport();
        function getweatherreport() {
            fetch(`https://api.covid19api.com/summary`)

                .then(coviddata => {
                    return coviddata.json();
                }).then(showreport);
        }

        function getid(city, coviddata) {
            for (var i = 0; i < coviddata.Countries.length; i++) {
                if (coviddata.Countries[i].Country == city) {
                    console.log(i)
                    return i
                }
            }

        }
        function showreport(coviddata) {
            let city = searchinputbox.value
            main_key = getid(city, coviddata);
            console.log(main_key)

            console.log(coviddata)

            console.log(coviddata.Countries[main_key].Country)
            console.log(coviddata.Countries[main_key].NewConfirmed)
            console.log(coviddata.Countries[main_key].TotalConfirmed)
            console.log(coviddata.Countries[main_key].TotalRecovered)

            let glocase = document.getElementById('globalcase');
            glocase.innerText = `${coviddata.Global.TotalConfirmed}`
            let glodet = document.getElementById('globaldeath');
            glodet.innerText = `${coviddata.Global.TotalDeaths}`
            let glorec = document.getElementById('globalrecoved');
            glorec.innerText = `${coviddata.Global.TotalRecovered}`

            let gloncase = document.getElementById('globalnewcase');
            gloncase.innerText = `${coviddata.Global.NewConfirmed}`
            let glondet = document.getElementById('globalnewdeath');
            glondet.innerText = `${coviddata.Global.NewDeaths}`
            let glonrec = document.getElementById('globalnewrecoverd');
            glonrec.innerText = `${coviddata.Global.NewRecovered}`

            let couname = document.getElementById('counameid');
            couname.innerText = `${coviddata.Countries[main_key].Country} , ${coviddata.Countries[main_key].CountryCode}`

            let councase = document.getElementById('newcountrycases');
            councase.innerText = `${coviddata.Countries[main_key].NewConfirmed}`
            let coundet = document.getElementById('newcountrydeaths');
            coundet.innerText = `${coviddata.Countries[main_key].NewDeaths}`
            let counrec = document.getElementById('newcountryrecoved');
            counrec.innerText = `${coviddata.Countries[main_key].NewRecovered}`

            let coucase = document.getElementById('countrycases');
            coucase.innerText = `${coviddata.Countries[main_key].TotalConfirmed}`
            let coudet = document.getElementById('countrydeaths');
            coudet.innerText = `${coviddata.Countries[main_key].TotalDeaths}`
            let courec = document.getElementById('countryrecoverd');
            courec.innerText = `${coviddata.Countries[main_key].TotalRecovered}`



        }
