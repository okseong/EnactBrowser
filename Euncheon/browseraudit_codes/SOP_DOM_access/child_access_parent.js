function() {
    var thisTest = this;
    $.get("/sop/pass/1", function() {
      $("<iframe>", {
        src: "https://browseraudit.org/sop/c2p/parent/none/aHR0cHM6Ly9icm93c2VyYXVkaXQuY29tL3NvcC9jMnAvY2hpbGQvMS9ub25lL2ZhaWw="
      }).appendTo("div#sandbox").load(function() {
        $.get("/sop/result/1", function(result) {
          if (result === "pass") {
            thisTest.PASS("The child iframe was unable to access the parent iframe's DOM.");
          } else {
            thisTest.CRITICAL("The child iframe was able to access the parent iframe's DOM.");
          }
        });
      });
    });
  }