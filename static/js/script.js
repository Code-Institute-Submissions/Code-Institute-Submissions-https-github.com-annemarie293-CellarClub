$(document).ready(function(){
    //Jquery for Mobile navbar collapse (Materialize)
    $('.sidenav').sidenav();
    //Jquery for Modal on Wines page (Materialize)
    $('.modal').modal();
    //Jquery for select option on forms (Materialize)
    $('select').formSelect();
    //Jquery for datepicker option on forms (Materialize)
    $('.datepicker').datepicker({
      format: "yyyy-mm-dd",
      yearRange: [1920,2021],
      showClearBtn: true,
      i18n: {
        done: "Select"
      }
    });
  });