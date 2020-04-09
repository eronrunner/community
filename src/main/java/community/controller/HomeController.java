/**
 * 
 */
package community.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * @author Nice Dream Er
 *
 */
@RestController
@RequestMapping("/")
public class HomeController {
	
	@GetMapping
	public String index() {
		return "index";
	}
}
