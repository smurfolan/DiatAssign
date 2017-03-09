using System.ComponentModel.DataAnnotations;

namespace DiatAssign.Models
{
    public class NewUserVm
    {
        public int? Age { get; set; }

        [Required]
        [StringLength(25)]
        public string FirstName { get; set; }

        [Required]
        [StringLength(25)]
        public string LastName { get; set; }
    }
}