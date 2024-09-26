document.addEventListener('DOMContentLoaded', function() {
    const deleteLinks = document.querySelectorAll('.btn-delete');
  
    deleteLinks.forEach(link => {
      link.addEventListener('click', function(e) {
        e.preventDefault();
        const modal = new bootstrap.Modal(document.getElementById('deleteConfirmationModal'));
        modal.show();
  
        document.getElementById('confirmDeleteBtn').addEventListener('click', function() {
          const input = document.getElementById('deleteInput');
          if (input.value.toUpperCase() === 'DELETE') {
            window.location.href = `/spell_delete/${link.dataset.spellId}/`;
          }
        });
  
        document.getElementById('deleteConfirmationModal').addEventListener('hidden.bs.modal', function () {
          document.getElementById('confirmDeleteBtn').removeEventListener('click', confirmDelete);
        });
      });
    });
  });