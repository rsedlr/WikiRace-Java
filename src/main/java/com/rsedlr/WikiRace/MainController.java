package com.rsedlr.WikiRace;

// import org.springframework.web.bind.annotation.RestController;
// import org.springframework.web.bind.annotation.RequestMapping;

// @RestController
// public class MainController {

//     @RequestMapping("/")
//     public String index() {
//         return "Greetings from Spring Boot!";
//     }

// }


import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class MainController {
   @RequestMapping(value = "/")
   public String index() {
      return "index";
   }
}