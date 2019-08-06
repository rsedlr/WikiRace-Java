package com.rsedlr.WikiRace;

// import org.springframework.web.bind.annotation.RestController;
// import org.springframework.web.bind.annotation.RequestMapping;


// @RestController
// public class SearchController {

//     @RequestMapping(value = "/wikiRace/search", method = RequestMethod.POST)
//     public String index() {
//         return "Greetings from Spring Boot!";
//     }

// }

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

@Controller
public class SearchController {

    // @GetMapping("/greeting")
    // public String greetingForm(Model model) {
    //     model.addAttribute("greeting", new Greeting());
    //     return "greeting";
    // }

    @PostMapping("/wikirace/search")
    public String searchSubmit(@ModelAttribute Greeting greeting) {
        return "result";
    }

}