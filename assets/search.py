''' ---------- TODO: REDO BREADTH FIRST SEARCH ---------- '''


def searchDatabase(database, startID, endID):
  print(startID)
  print(endID)

  if startID == endID:
    return [startID]
  

  paths = []
  unvisited_forward = {startID: [None]}
  unvisited_backward = {endID: [None]}
  visited_forward = {}
  visited_backward = {}
  forward_depth = 0
  backward_depth = 0

  ''' main search loop '''
  while (len(paths) == 0) and ((len(unvisited_forward) != 0) and (len(unvisited_backward) != 0)):
    
    forward_links_count = database.getLinksCount('out', unvisited_forward.keys())
    backward_links_count = database.getLinksCount('in', unvisited_backward.keys())

    #-------------------- FORWARD BREADTH FIRST SEARCH --------------------#
    if forward_links_count < backward_links_count:   
      forward_depth += 1
      outgoing_links = database.getLinks('out', unvisited_forward.keys())  # Fetch the pages which can be reached from the currently unvisited forward pages.

      for page_id in unvisited_forward:  # Mark all of the unvisited forward pages as visited.
        visited_forward[page_id] = unvisited_forward[page_id]

      unvisited_forward.clear()  # Clear the unvisited forward dictionary.

      for source_page_id, target_page_ids in outgoing_links:
        for target_page_id in target_page_ids.split('|'):
          if target_page_id:
            target_page_id = int(target_page_id)
            if (target_page_id not in visited_forward) and (target_page_id not in unvisited_forward):  # If the target page is in neither visited forward nor unvisited forward, add it to unvisited forward.
              unvisited_forward[target_page_id] = [source_page_id]
            elif target_page_id in unvisited_forward:  # If the target page is in unvisited forward, add the source page as another one of its parents.
              unvisited_forward[target_page_id].append(source_page_id)
    
    #--------------------  BACKWARD BREADTH FIRST SEARCH  --------------------#
    else:  
      backward_depth += 1
      incoming_links = database.getLinks('in', unvisited_backward.keys())  # Fetch the pages which can reach the currently unvisited backward pages.

      for page_id in unvisited_backward:  # Mark all of the unvisited backward pages as visited.
        visited_backward[page_id] = unvisited_backward[page_id]

      unvisited_backward.clear()  # Clear the unvisited backward dictionary.

      for target_page_id, source_page_ids in incoming_links:
        for source_page_id in source_page_ids.split('|'):
          if source_page_id:
            source_page_id = int(source_page_id)
            if (source_page_id not in visited_backward) and (source_page_id not in unvisited_backward):  # If the source page is in neither visited backward nor unvisited backward, add it to unvisited backward.
              unvisited_backward[source_page_id] = [target_page_id]
            elif source_page_id in unvisited_backward:  # If the source page is in unvisited backward, add the target page as another one of its parents.
              unvisited_backward[source_page_id].append(target_page_id)


    #--------------------  CHECK FOR PATH COMPLETION  --------------------#
    for page_id in unvisited_forward:  # The search is complete if any of the pages are in both unvisited backward and unvisited, so find the resulting paths.
      if page_id in unvisited_backward:
        paths_from_source = get_paths(unvisited_forward[page_id], visited_forward)
        paths_from_target = get_paths(unvisited_backward[page_id], visited_backward)

        for path_from_source in paths_from_source:
          for path_from_target in paths_from_target:
            current_path = list(path_from_source) + [page_id] + list(reversed(path_from_target))

            # TODO: This line shouldn't be required, but there are some unexpected duplicates.
            if current_path not in paths:
              paths.append(current_path)

  return paths


def get_paths(page_ids, visited_dict):
  """Returns a list of paths which go from the provided pages to either the source or target pages.

  Args:
    page_ids: The list of page IDs whose paths to get.

  Returns:
    list(list(int)): A list of lists of page IDs corresponding to paths from the provided page IDs
      to the source or target pages.
  """
  paths = []

  for page_id in page_ids:
    if page_id is None:
      # If the current page ID is None, it is either the source or target page, so return an empty
      # path.
      return [[]]
    else:
      # Otherwise, recursively get the paths for the current page's children and append them to
      # paths.
      current_paths = get_paths(visited_dict[page_id], visited_dict)
      for current_path in current_paths:
        new_path = list(current_path)
        new_path.append(page_id)
        paths.append(new_path)

  return paths


