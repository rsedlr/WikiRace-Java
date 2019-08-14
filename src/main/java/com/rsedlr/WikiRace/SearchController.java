package com.rsedlr.WikiRace;

import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
// import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RequestBody;

import org.springframework.stereotype.Controller;
// import org.springframework.ui.Model;

// package com.testmockmvc.testrequest.controller;
// import org.apache.commons.io.IOUtils;
// import javax.servlet.http.HttpServletRequest;
import java.io.IOException;


@RestController
public class SearchController {

    @RequestMapping(path = "/wikiRace/search", method = RequestMethod.POST)
    public String[] recieveSearch(@RequestBody String request) throws IOException {
        System.out.println("");
        System.out.println(request);
        System.out.println("");
        // String[] test = {"yes","no"};
        String test[] = new String[] {"yes","no"};
        return test;
    }

    // @RequestMapping(path = "/wikirace/search", method = RequestMethod.POST)
    // public String testGetRequest(@RequestBody String request) throws IOException {
    //     final byte[] requestContent;
    //     requestContent = IOUtils.toByteArray(request.getReader());
    //     return new String(requestContent, StandardCharsets.UTF_8);
    // }
}


