using System.ComponentModel.DataAnnotations;

namespace DiatAssign.Models
{
    public class UserVm
    {
        public int Id { get; set; }
        
        public int? Age { get; set; }

        [Required]
        [StringLength(25)]
        public string FirstName { get; set; }

        [Required]
        [StringLength(25)]
        public string LastName { get; set; }
    }
}