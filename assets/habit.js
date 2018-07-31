
    function add_habit_form(event, plan_id) {
        console.log('called');
        var url = ADD_HABIT;
        {#$('#loaderdiv').show();#}

        $.get(url, {}, function (res) {
            {#$('#loaderdiv').hide();#}

            if (res) {
                console.log(res);
                $('#add_new_habit').html(res).modal({
                    keyboard: true,
                    toggle: true,
                    show: true,
                    backdrop: true,
                    hide: true
                });
            } else {
                alert('No details found.');
            }

        });
    }
