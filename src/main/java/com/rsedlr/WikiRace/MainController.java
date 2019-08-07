package com.rsedlr.WikiRace;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

// import org.springframework.web.bind.annotation.RestController;
// import org.springframework.web.bind.annotation.RequestMapping;


@Controller
public class MainController {
    @RequestMapping(value = "/wikiRace")
    public String index() {
        return "race";
    }

}

