function add_habit_form() {
    fetch(ADD_HABIT)
        .then(res=>{return res.text()})
        .then(res => {
             $('#add_new_habit_dialog').html(res);
        });
}


