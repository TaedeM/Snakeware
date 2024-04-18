using Microsoft.AspNetCore.Mvc;

namespace PrimeCheckerAPI.Controllers
{
    [ApiController]
    [Route("api")]
    public class DefaultController : ControllerBase
    {
        // Default route, displays '{}' at /api/
        [HttpGet]
        public IActionResult Default()
        {
            return Ok(new {});
        }
    }
    
    [Route("api/[controller]")]
    public class NumberController : ControllerBase
    {
        // Default route, displays '{}' at /api/number/
        [HttpGet]
        public IActionResult Default()
        {
            return Ok(new {});
        }

        // Route when an input number is given
        [HttpGet("{number}")]
        public IActionResult CheckNumber(long number)
        {
            var result = new Dictionary<string, object>
            {
                { "input_number", number },
                { "prime", IsPrime(number) },
                { "fibonacci", IsFibonacci(number) }
            };

    	    return Ok(result);

        }

        // Use 'long' instead of 'int' as 'int' is too small for high Fibonacci numbers
        private bool IsPrime(long number)
        // Adapted function 'is_prime' from '../../python/app.py' to C#
        {
            if (number < 2)
            {
                return false; // Numbers less than 2 are not prime
            }

            for (long i = 2; i <= Math.Sqrt(number); i++)
            {
                if (number % i == 0)
                {
                    return false; // Number is not prime
                }
            }

            return true; // Number is prime
        }

        private bool IsFibonacci(long number)
        // Adapted function 'is_fibonacci' from ''../../python/app.py' to C#
        {
            // Base case
            if (number == 0 || number == 1)
            {
                // 0 and 1 are part of the Fibonacci sequence
                return true;
            }

            // Initialization
            int max_iter = 52;
            long n1 = 0, n2 = 1;
            int counter = 1;

            // Check if number is in Fibonacci sequence
            while (n2 < number && counter < max_iter)
            {
                counter++;                
                long temp = n1;
                n1 = n2;
                n2 = temp + n2;

                if (n2 == number)
                {
                    return true; // number is in the Fibonacci sequence
                }
            }

            return false; // number is not in the Fibonacci sequence
        }
    }
}
