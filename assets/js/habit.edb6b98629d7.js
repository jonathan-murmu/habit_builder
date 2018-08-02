function add_habit_form() {
    console.log('habit form');
    console.log(ADD_HABIT)
    fetch(ADD_HABIT)
        .then(res=>{return res.text()})
        .then(res => {
             $('#add_new_habit_dialog').html(res);
        });
}


