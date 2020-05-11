
var cookiesAccepted = window.localStorage.getItem("cookiesAccepted") ? window.localStorage.getItem("cookiesAccepted") : window.sessionStorage.getItem("cookiesAccepted");

var theme = window.localStorage.getItem("theme") ? window.localStorage.getItem("theme") : window.sessionStorage.getItem("theme");

// The following 2 functions are used inline due to the dinamic reloading of comments
// Function to confirm deletion of comments with modal box
function confirmation(button) {
  var divID = "#" + $(button).attr("data-id");
  $(divID + ".comment-confirm-overlay").css("display", "flex");
};

// Function to cancel the deletion modal box
function cancel(button) {
  $(button).parents(".comment-confirm-overlay, .ticket-confirm-overlay").fadeOut();
};

// Changing colour theme on the body based on the setting saved
if (theme) {
  document.body.className = theme;

  // Changing the theme switch widget according to the theme
  if (theme === "dark" && $(".theme-switch")) {
    $(".theme-switch").addClass("dark-theme");
    $("meta[name='theme-color']").attr("content", "#3F3E39");
  };
};

$(document).ready(function () {

  // Moving user's layout, theme, cookies settings to localStorage if cookies are accepted
  $(".accept").click(function () {

    $(Object.keys(window.sessionStorage)).each(function () {
      window.localStorage.setItem(this, window.sessionStorage.getItem(this));
    });

    window.sessionStorage.clear();
    window.localStorage.setItem("cookiesAccepted", "true");
    $(".cookie-banner").fadeOut();

    // Changing buttons on Account page if cookies are accepted on that page
    $(".cookies .accept").html("<i class='far fa-check-circle'></i> Accepted").css("box-shadow", "var(--shadow-inset)");
    $(".cookies .decline").html("Decline").css({"box-shadow": "", "color": ""});
  });

  // Moving user's layout, theme, cookies settings to sessionStorage if cookies are declined
  $(".decline").click(function () {

    $(Object.keys(window.localStorage)).each(function () {
      window.sessionStorage.setItem(this, window.localStorage.getItem(this));
    });

    window.localStorage.clear();
    window.sessionStorage.setItem("cookiesAccepted", "false");
    $(".cookie-banner").fadeOut();

    // Changing buttons on Account page if cookies are declined on that page
    $(".cookies .accept").html("Accept").css("box-shadow", "");
    $(".cookies .decline").html("<i class='far fa-times-circle'></i> Declined").css({"box-shadow": "var(--shadow-inset)", "color": "var(--font-colour)"});
  });

  // Clearing sessionStorage on logout
  $(".logout").click(function () {
    window.sessionStorage.clear();
  });

  // Changing buttons on Account page if cookies are already accepted or declined
  if (cookiesAccepted === "true") {
    $(".cookies .accept").html("<i class='far fa-check-circle'></i> Accepted").css("box-shadow", "var(--shadow-inset)");
    $(".cookies .decline").html("Decline").css({"box-shadow": "", "color": ""});
  } else if (cookiesAccepted === "false") {
    $(".cookies .accept").html("Accept").css("box-shadow", "");
    $(".cookies .decline").html("<i class='far fa-times-circle'></i> Declined").css({"box-shadow": "var(--shadow-inset)", "color": "var(--font-colour)"});
  };

  // Showing cookies message if choice hasn't been made yet and the window is not a contentWindow
  if (!cookiesAccepted && !window.frameElement && location.href !== "https://etracker.eu.pythonanywhere.com/") {
    $(".cookie-banner").show();
  };

  if (window.location.href === "https://etracker.eu.pythonanywhere.com/?next=/home/") {
    $(".cookie-banner").hide();
  };

  // Contact links pop-up modal box
  $("#contact").click(function () {
    $("#contact-overlay").css("display", "flex");
  });

  // Hiding modal boxes on clicking anywhere outside of the content or on "close" icon
  $(window).click(function(event) {
    if (event.target.id === "contact-overlay" || event.target.id === "close" || event.target.id === "positions-overlay") {
      $("#contact-overlay").fadeOut();
      $("#positions-overlay").fadeOut();
    };
  });

  // Back to top icon in the bottom right corner on scroll
  $(window).on("scroll", function () {

    if ($("html, body").scrollTop() > 100 || window.scrollY > 100 || window.pageYOffset > 100 || document.documentElement.scrollTop > 100 || document.body.scrollTop > 100) { 
      $("#back-to-top").fadeIn();
    } else {
      $("#back-to-top").fadeOut();
    };
  });

  // Animating "back to top" when clicking the icon
  $("#back-to-top").click(function () {
    $("html, body").animate({ scrollTop: "0" });
  });

  // Changing colour theme with theme switch widget
  $(".theme-switch").click(function () {

    $("body").toggleClass("light");
    $("body").toggleClass("dark");

    $("iframe").contents().find("body").toggleClass("light");
    $("iframe").contents().find("body").toggleClass("dark");

    $(this).toggleClass("dark-theme");

    // Changing colour for address bar
    if ($(".theme-switch").hasClass("dark-theme")) {
      $("meta[name='theme-color']").attr("content", "#3F3E39");
    } else {
      $("meta[name='theme-color']").attr("content", "#F2EEDA");
    };

    // Saving theme setting to browser storage
    if (window.localStorage.getItem("cookiesAccepted") === "true") {
      window.localStorage.setItem("theme", document.body.className);
    } else {
      window.sessionStorage.setItem("theme", document.body.className);
    };
  });

  $(":not(header)").on("dragstart drop", function (event) {
    event.preventDefault();
  });

  // Drag and drop funcionality to the sections on Home page via their header
  $(".drop-container > section > header").each(function () {
    var parentId = $(this).parents("section").attr("id");
    var parentSection = $(this).parents("section");

    $(this).attr("draggable", "true");

    $(this).on("dragstart", function (event) {
      var image = this.parentElement;
      var parentOffset = parentSection.offset();
      var positionX = event.pageX - parentOffset.left;
      var positionY = event.pageY - parentOffset.top;

      event.stopPropagation();
      event.originalEvent.dataTransfer.setData("text", parentId);
      event.originalEvent.dataTransfer.effectAllowed = "move";
      event.originalEvent.dataTransfer.setDragImage(image, positionX, positionY);
      parentSection.css("filter", "opacity(0.5)");
    });

    $(this).on("dragend", function () {
      parentSection.css("filter", "");
    });
  });

  $(".drop-container").each(function(index) {
    var id = $(this).attr("id");
    var currentSection = $(this).find("section").attr("id");
    var inLocal = window.localStorage.getItem(id) ? window.localStorage.getItem(id) : currentSection;
    var inSession = window.sessionStorage.getItem(id) ? window.sessionStorage.getItem(id) : currentSection;
    
    // Swapping sections and saving position based on previous user settings
    if (window.localStorage.getItem("cookiesAccepted") === "true") {

      if (currentSection !== inLocal) {
        var moveTo = $("#" + inLocal).parents(".drop-container");
        var swapped = $("#" + currentSection).replaceWith($("#" + inLocal));
        moveTo.append(swapped);
      };

      window.localStorage.setItem(id, $(this).find("section").attr("id"));

    } else {
      
      if (currentSection !== inSession) {
        var moveTo = $("#" + inSession).parents(".drop-container");
        var swapped = $("#" + currentSection).replaceWith($("#" + inSession));
        moveTo.append(swapped);
      };

      window.sessionStorage.setItem(id, $(this).find("section").attr("id"));
    };

    // Loading sections one after the other
    $(this).fadeIn((1 + index) * 250);

    $(this).on("dragover", function (event) {
      event.preventDefault();
    });

    // Drop part of drag & drop including swapping sections
    $(this).on("drop", function(event) {
      event.preventDefault();
      var data = event.originalEvent.dataTransfer.getData("text");

      if (data) {
        var toMove = $(this).find("section");
        var moveTo = $(this);
        var moveFrom = $("#" + data).parents(".drop-container");

        moveFrom.append(toMove);
        moveTo.append($("#" + data));

        // Saving changes to browser storage
        if (window.localStorage.getItem("cookiesAccepted") === "true") {
          window.localStorage.setItem(moveTo.attr("id"), data);
          window.localStorage.setItem(moveFrom.attr("id"), toMove.attr("id"));
        } else {
          window.sessionStorage.setItem(moveTo.attr("id"), data);
          window.sessionStorage.setItem(moveFrom.attr("id"), toMove.attr("id"));
        };
      };

      event.originalEvent.dataTransfer.clearData();
    });
  });

  // Showing "drag & drop" icon only if pointer device is available and on mouseenter
  $("section > header").each(function () {
    $(this).on("mouseenter", function () {

      if ($(this).children(".fa-arrows-alt").css("display") === "none" && window.matchMedia("(pointer: fine)").matches) {
        $(this).children(".fa-arrows-alt").show();
      };
    });

    $(this).on("mouseleave", function () {
      $(this).children(".fa-arrows-alt").fadeOut("fast");
    });
  });

  // Changing section positions with click on icon if pointer device is not available
  var sectionId, containerId;
  $(".fa-arrows-alt-v, .fa-arrows-alt").each(function () {
    $(this).click(function () {
      
      // Getting section and container numbers where the icon is for the swap later
      sectionId = $(this).parents("section").attr("id");
      containerId = $(this).parents(".drop-container").attr("id");
      
      // Positions list pop-up modal box
      $("#positions-overlay").css("display", "flex");

      // Checking only the current position number
      $("[name='position']").attr("checked", false);
      $("input[value='" + containerId + "']").attr("checked", true);
    });
  });

  // Swapping saved positions of sections and reloading the page when choosing new position number
  $("[name='position']").each(function () {
    $(this).click(function () {
      var toMove = $("#" + this.value).find("section").attr("id");

      if (window.localStorage.getItem("cookiesAccepted") === "true") {

        window.localStorage.setItem(this.value, sectionId);
        window.localStorage.setItem(containerId, toMove);
        window.location.reload();

      } else {
        
        window.sessionStorage.setItem(this.value, sectionId);
        window.sessionStorage.setItem(containerId, toMove);
        window.location.reload();
      };
    });
  });

  // Opening details of each ticket as an accordion by clicking on the row
  $(".accordion").each(function () {
    $(this).click(function () {

      $(this).toggleClass("active"); //Highlighting the row opened
      $(this).next().children(".container-2").fadeToggle("slow");
      $(this).next().slideToggle("slow");

      // Hiding all open iframes if accordion is closed
      if ($(this).hasClass("active") === false) {
        $(this).next().find(".container-1, .container-2, iframe").fadeOut("slow");
      };
    });
  });

  // Opening/closing iframe with the corresponding page on clicking the "Edit", "Add comment" or "Change password" button
  $(".edit-link").each(function () {
    $(this).click(function () {
      var nextIframe = $(this).parent().next().children("iframe");

      nextIframe.fadeToggle("slow", function () {
        $(".password-iframe").contents().blur(); //To be able to autofocus the first input field on Change Password page
      });

      $(nextIframe).parent().slideToggle("slow");
    });
  });

  // Resizing iframes to the height of the form in the contentWindow and hiding their footer
  if (window.frameElement) {
    var formHeight = $(this).find("form").css("height");
    
    $("footer").hide();
    $("#wrapfabtest").hide();
    $(window.frameElement).animate({ height: formHeight });
  };

  // Closing iframe when clicking "Cancel"
  $(".edit-form :reset, .password-form :reset").click(function () {
      $(window.frameElement).fadeOut();
      $(window.frameElement).parent().slideUp("slow");
  });

  // Reloading the page after editing a ticket and clicking "Save"
  $(".reload").click(function () {
    window.parent.location.reload(forceGET=true);
    $(window.frameElement).fadeOut(200);
    $(window.frameElement).parent().fadeOut(150);
  });

  // Dinamically reloading comments, their header with the count and the deletion confirmation modal boxes after adding a new comment
  $(".comment-form :submit").each(function () {
    $(this).click(function () {
      var id = "#" + window.frameElement.name;

      window.parent.$(id).load("# " + id + " > *");
      window.parent.$(id + "_head").children("h4").load("# " + id + "_head h4:first-child");
      window.parent.$("#confirmation-boxes").load("# #confirmation-boxes > *");
    });
  });

  // Confirming deletion of a ticket with modal box
  $(".ticket-confirmation").each(function () {
    $(this).click(function () {
      var divID = "#" + $(this).attr("data-id");

      $(divID + ".ticket-confirm-overlay").css("display", "flex");
    });
  });

  // Making the "Description" helptext a placeholder instead
  $("#id_description").attr("placeholder", $("#id_description").next(".helptext").text());

  // Changing the django default label for new password confirmation
  $("label[for='id_new_password2']").text("Confirm password:");

  // Autofocusing on the first input field of the password change form and on the comment text field
  $("#id_text, #id_old_password").focus();

  // Autofocus for the search bar on Tickets page
  $("#search-bar input").mouseenter(function () {
    $(this).focus();
  });

  // Filter funcionality with the search bar on Tickets Page
  $("#search-bar input").on("keyup input", function () {
    var input = $("#search-bar input").val().toUpperCase().replace(/\s+/g, "");

    $(".accordion").each(function () {
      var detailsTxt = $(this).next().find(".details > .wide").text().toUpperCase().replace(/DELETE COMMENT/g, "").replace(/\s+/g, "");
      var txtValues = $(this).text().toUpperCase().replace(/\s+/g, "") + detailsTxt;

      if (txtValues.includes(input)) {
        $(this).show();

        // The corresponding header on small screen
        if (window.matchMedia("(max-width: 640px)").matches) {
          $(this).prev(".hidden").show();
        }
      } else {
        $(this).hide();

        // Hiding all open iframes, details too and removing highlight if it was open
        $(this).removeClass("active");
        $(this).next().hide();
        $(this).next().find(".container-1, .container-2, iframe").hide();

        // Hiding the corresponding header on small screen
        if (window.matchMedia("(max-width: 640px)").matches) {
          $(this).prev(".hidden").hide();
        }
      }
    });
  });
});
